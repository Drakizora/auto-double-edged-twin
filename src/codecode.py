import html
import customize

# Imports the raw copy/paste contents from Discord
def get_discord_posts():
  f = open('./input.txt', 'r')
  return f.read()

# Writes the given content to a text file
def export(content : str):
  with open("output.txt", "w") as f:
    f.write(content)
    
# Matches the name to the list of characters. Returns narrator if it cannot be matched. 
def search_name(name : str):
  lists = customize.clans
  # Check every list
  for l in lists.keys():
    # Check every name
    for n in lists[l]:
      # Does this name match what was given from Discord?
      if n in name:
        return n, l 

  return "narrator", None
    
# Returns full info on the character
def read_config(character : str):
  name, lst = search_name(character)
  
  if name == "narrator":
    return {"name": "narrator"}
        
  clan = customize.BREEZECLAN if "breezeclan" in lst else customize.MARSHCLAN
  status = "players" if "players" in lst else "npcs"
  icons = customize.icons
  icon = icons.get(name, icons[clan])
  color = customize.colors[status]
      
  config = {
    "name": name,
    "clan": clan,
    "status": status,
    "icon": icon,
    "color": color
  }
  
  return config

# Create post data
def get_post(content : list):
  character = content[0].lower()
  details = read_config(character)
  
  text = ""
  count = 0
  
  for p in content[3:]:
    if p != "":
      text = text + f"\n\t<p>\n\t\t{p}\n\t</p>"
      count = count + len(p.split())
  
  details.update({
    "post": text,
    "words": count
  })
  
  return details

# Parses and formats the input
def parse():
  content = get_discord_posts()
  lines = content.split("\n")
  
  posts = []
  start = None
  end = 0
  
  for i in range(len(lines)):
    if lines[i] == "APP":
      if start is None:
        start = i-1
      else:
        end = i-1
        posts.append(get_post(lines[start:end]))
        start = end
  posts.append(get_post(lines[end:]))
  
  return posts

# Creates the html code
def create_html(posts : dict):
  full_html = ""
  html_posts = ""
  html_count = ""
  wordcount = {}
  
  for p in posts:
    if p["name"] == "narrator":
      content = html.narration.format(content=p["post"])
      
    else:
      count = wordcount.get(p["name"], 0) + p["words"]
      wordcount.update({p["name"] : count})
        
      if p["clan"] == customize.YOUR_CLAN:
        content = html.left.format(
          color=p["color"],
          name=p["name"],
          icon=p["icon"],
          content=p["post"],
          bootstrap=None if customize.USE_CUSTOM_COLORS else "text-muted"
        )
        
      else:
        content = html.right.format(
          color=p["color"],
          name=p["name"],
          icon=p["icon"],
          content=p["post"],
          bootstrap=None if customize.USE_CUSTOM_COLORS else "text-muted"
        )
        
    html_posts = html_posts + content + "\n"
  
  for c in wordcount.keys():
    
    content = html.stardust.format(
      name=c,
      words=wordcount[c]
    )
    
    html_count = html_count + content + "\n"
  
  full_html = html.outer.format(
    content=html_posts,
    stardust=html_count
  )
    
  return full_html


try:
  posts = parse()
  pretty_html = create_html(posts)
  export(pretty_html)
  print("all done!")

except Exception as e:
  print("something has tragically gone wrong")
  print(e)
