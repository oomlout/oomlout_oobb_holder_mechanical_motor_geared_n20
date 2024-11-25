import copy
import opsc
import oobb
import oobb_base
import yaml
import os

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "test"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        navigation = False
        #navigation = True    

        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 3
        kwargs["height"] = 1
        kwargs["thickness"] = 12
        
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "test" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 12
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)

        part = copy.deepcopy(part)
        p3 = copy.deepcopy(part["kwargs"])
        p3["extra"] = "clearance_cutout"
        part["kwargs"] = p3        
        parts.append(part)

        part = copy.deepcopy(part)
        p3 = copy.deepcopy(part["kwargs"])
        p3["thickness"] = 30
        part["kwargs"] = p3        
        parts.append(part)

        part = copy.deepcopy(part)
        p3 = copy.deepcopy(part["kwargs"])
        p3["extra"] = "clearance_cutout"
        part["kwargs"] = p3        
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 3
        p3["height"] = 3
        p3["thickness"] = 12
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)

        part = copy.deepcopy(part)
        p3 = copy.deepcopy(part["kwargs"])
        p3["thickness"] = 30
        part["kwargs"] = p3
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 3
        p3["height"] = 3
        p3["thickness"] = 3.7
        p3["extra"] = "holder"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)


        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")


    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        generate_navigation(sort = sort)

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    if height == 3 and width == 3 and extra == "holder":
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        locations = []
        locations.append([1,2])
        locations.append([1,3])
        locations.append([2,3])
        locations.append([3,2])
        locations.append([3,3])
        p3["radius_name"] = "m6"
        p3["locations"] = locations 
        p3["holes"] = ["single"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        p4["radius_name"] = "m3"
        locations = []
        locations.append([1,2.5])
        locations.append([1.5,3])
        locations.append([2.5,3])
        locations.append([1,2.5])
        locations.append([2,2.5])
        locations.append([3,2.5])
        p4["locations"] = locations
        oobb_base.append_full(thing,**p4)
    else:    
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        if height == 1:
            p3["holes"] = ["top","bottom"]
        else:
            p3["holes"] = ["perimeter"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        

        
       


    #add cutout for motor
    if extra == "" or extra == "clearance_cutout":
        thing = add_mechanical_motor_geared_n20(thing, **kwargs)
    elif extra == "holder":
        thing = add_mechanical_motor_geared_n20_holder(thing, **kwargs)
    
    if extra == "clearance_cutout":
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 12
        h = 14
        d = 6
        p3["size"] = [w,h,d]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -16
        pos1[2] += depth
        pos2 = copy.deepcopy(pos)
        pos2[0] += 16
        pos2[2] += depth
        poss = []
        poss.append(pos1)
        poss.append(pos2)
        p3["pos"] = poss
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)


    #add extra cutout if deep
    if depth > 12:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        
        w = 22
        h = 11
        if height == 3:
            h = 22
        d = depth - 6
        p3["size"] = [w,h,d]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #add wire cutout
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 3
        h = width * 15
        d = 3
        p3["size"] = [w,h,d]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def add_mechanical_motor_geared_n20_holder(thing, **kwargs):

    
    pos = kwargs.get("pos", [0, 0, 0])
    rot = kwargs.get("rot", [0, 0, 0])
    depth = kwargs.get("thickness", 3)

    position_holder = [0,-22,0]
    #add screw_countersunk
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m3"
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[0] += position_holder[0] + 13.5
    pos1[1] += position_holder[1] + 10
    pos1[2] += position_holder[2] 
    pos2 = copy.deepcopy(pos)
    pos2[0] += position_holder[0] - 13.5
    pos2[1] += position_holder[1] + 10
    pos2[2] += position_holder[2]
    poss = []
    poss.append(pos1)
    poss.append(pos2)
    p3["pos"] = poss
    rot1 = copy.deepcopy(rot)
    rot1[1] = 180
    p3["rot"] = rot1
    oobb_base.append_full(thing,**p3)


    return thing

def add_mechanical_motor_geared_n20(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        positions = []
        positions.append([4.5,0,0])
        positions.append([-4.5,0,0])

        for position in positions:
            #add screw_countersunk
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_screw_countersunk"
            p3["radius_name"] = "m1_6"
            depth_screw_connector = 4
            p3["depth"] = depth_screw_connector
            #p3["m"] = "#"        
            pos1 = copy.deepcopy(pos)
            pos1[0] += position[0]
            pos1[1] += position[1]
            pos1[2] += position[2] + depth
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)

        #add motor cutout
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        ex = 2
        w = 12 + ex
        h = 9 + ex
        flange_thickness = 1.5
        d = depth - depth_screw_connector + flange_thickness
        p3["size"] = [w,h,d]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)


        #add hole in middle
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        p3["radius_name"] = "m4"
        p3["depth"] = depth
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        return thing


###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    
    folder = f"scad_output/{thing['id']}"

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        

        opsc.opsc_make_object(f'{folder}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)  

    yaml_file = f"{folder}/working.yaml"
    with open(yaml_file, 'w') as file:
        yaml.dump(part, file)

def generate_navigation(folder="scad_output", sort=["width", "height", "thickness"]):
    #crawl though all directories in scad_output and load all the working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if 'working.yaml' in files:
            yaml_file = os.path.join(root, 'working.yaml')
            with open(yaml_file, 'r') as file:
                part = yaml.safe_load(file)
                # Process the loaded YAML content as needed
                part["folder"] = root
                part_name = root.replace(f"{folder}","")
                
                #remove all slashes
                part_name = part_name.replace("/","").replace("\\","")
                parts[part_name] = part

                print(f"Loaded {yaml_file}: {part}")

    pass
    for part_id in parts:
        part = parts[part_id]
        kwarg_copy = copy.deepcopy(part["kwargs"])
        folder_navigation = "navigation"
        folder_source = part["folder"]
        folder_extra = ""
        for s in sort:
            ex = kwarg_copy.get(s, "default")
            folder_extra += f"{s}_{ex}/"

        #replace "." with d
        folder_extra = folder_extra.replace(".","d")            
        folder_destination = f"{folder_navigation}/{folder_extra}"
        if not os.path.exists(folder_destination):
            os.makedirs(folder_destination)
        if os.name == 'nt':
            #copy a full directory
            command = f'xcopy "{folder_source}" "{folder_destination}" /E /I'
            print(command)
            os.system(command)
        else:
            os.system(f"cp {folder_source} {folder_destination}")

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)