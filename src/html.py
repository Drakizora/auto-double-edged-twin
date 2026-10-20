narration = """
    <!--- NARRATION --->
    <div class = "row no-gutters mb-2">

        <!-- STAR ICON -->
        <div class="col-12 pb-2 text-center">
                            
            <i class="far fa-sparkle fa-sharp fa-fw" style="font-size:200%;"></i>
            
        </div>
    
        <!-- POST CONTENTS -->
        <div class = "col-12 col-md-11 mx-auto px-md-1 text-justify" style = "font-size:90%">
            {content}
        </div>
        
        <!-- DIVIDER -->
        <hr class = "col-12 mx-auto" style="border-top:1px solid !important;opacity:.5;">
        
    </div>
"""

left = """
    <!--- LEFT-POST --->
    <div class = "row no-gutters mb-2">

        <!-- CHARACTER NAME AND ICON -->
        <div class="col-12 col-md-2 pb-2">
                            
            <div class="text-center text-uppercase {bootstrap}" style="letter-spacing:1px; color: {color};">
                
                {name}
                
            </div>
            
            <div class="card border-0 rounded-0 flex-grow-1 p-1">
                <div class="h-100" style="min-height:5rem;background-repeat:no-repeat;
                
                    background-image:url('{icon}');
                    background-size:contain;
                    background-position:center;
                    
                "></div>
            </div>
            
        </div>
    
        <!-- POST CONTENTS -->
        <div class = "col-12 col-md px-md-1 text-justify" style = "font-size:90%">
            {content}
        </div>
        
        <!-- DIVIDER -->
        <hr class = "col-12 mx-auto" style="border-top:1px solid !important;opacity:.5;">
        
    </div>
"""

right = """
    <!--- RIGHT-POST --->
    <div class = "row no-gutters mb-2">

        <!-- CHARACTER NAME AND ICON -->
        <div class="col-12 col-md-2 pb-2">
                            
            <div class="text-center text-uppercase {bootstrap}" style="letter-spacing:1px; color: {color};">
                
                {name}
                
            </div>
            
            <div class="card border-0 rounded-0 flex-grow-1 p-1">
                <div class="h-100" style="min-height:5rem;background-repeat:no-repeat;
                
                    background-image:url('{icon}');
                    background-size:contain;
                    background-position:center;
                    
                "></div>
            </div>
            
        </div>
    
        <!-- POST CONTENTS -->
        <div class = "col-12 col-md px-md-1 text-justify order-md-first" style = "font-size:90%">
            {content}
        </div>
        
        <!-- DIVIDER -->
        <hr class = "col-12 mx-auto" style="border-top:1px solid !important;opacity:.5;">
        
    </div>
"""


stardust = """
    <div class = "pb-1">
        {name} {words} <span class = "text-muted">(+?<i class="fas fa-sparkles fa-fw"></i>)</span>
    </div>
"""


outer = """
<!---- COLORS

    PLAYER CHARACTERS: #879CB9
    NPCS: #C3B27B

---->


<div class = "container mx-auto" style = "font-family:avenir, serif;font-size:90%;">

    {content}
    
    <!-- WORD COUNT -->
    <div class = "row no-gutters mb-2">
        <div class = "col-12 col-md-6 mx-auto card rounded-0 text-center text-uppercase p-2" style = "font-size:90%;">
            <div>
                <i class="far fa-sparkle fa-sharp fa-fw" style="font-size:150%;"></i>
            </div>
            <div class = "pb-1 text-muted" style = "letter-spacing:.5px;">
                submission pending
            </div>
            
            {stardust}
        </div>
    </div>

    <!--- DRAKIZORA CODING CREDIT : DO NOT REMOVE --->
    <div class = "row no-gutters">
        <a href="https://toyhou.se/42284596." class="col-12 text-right faded text-muted">
          <i class="fas fa-dragon"></i><i class="fas fa-telescope"></i>
        </a>
    </div>
    
</div>
"""
