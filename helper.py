def get_firefox_path(file ="places.sqlite"):
    import sys
    import os
    
    folder = ""
    #MAC
    if sys.platform == "darwin":
        folder = os.path.expanduser("~") + "/Library/Application Supper/Firefox/Profiles/"
  
    #Linux    
    elif sys.platform.startswith("linux"):
        #sys.platform == linux, sys.platfoprm == linux 2
        folder = os.path.expanduser("~") + "/.mozilla/firefox/"
        
    #windows
    elif sys.platform == "win32" or sys.platform =="cyqwin":
        folder = os.path.expanduser("~") + "/AppData/Roaming/Mozilla/Firefox/Profiles/"
        
    profile = None
    profiles = os.listdir(folder)
    for element in profiles:
        if element == "Crash Reports":
            continue
        
        if element[0] ==".":
            continue
         #folder + "/" +element
        if os.path.isdir(folder + "/" + element):
            if os.path.isfile(folder + "/" + element + "/places.sqlite"):
                profile = element
                
        if profile == None:
            raise Exception("Firefox could not be found")
            
        return folder +  element  + "/"+ file      
       