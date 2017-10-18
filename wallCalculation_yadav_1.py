def wallcalculation_parallel(parallel_layer):
    Material_library= {"stucco_25mm":0.037,"facebrick_100mm":0.075,"Building paper":0.011,"insideSurface":0.12,"outsideSurfaceSummer":0.044,
    "outsideSurfaceWinter":0.03,"woodBevelLappedsliding_200mm":0.14,"woodFiberBoard_13mm":0.23,"gypsum_13mm":0.079,
    "glassFibreInsulation_25mm":2.52,"woodStud_90mm":0.63}
    
    parallel_layer=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","glassFibreInsulation_25mm","woodStud_90mm",
    "gypsum_13mm","insideSurface"]
    
    Rtot=0
    Rvalue_loop=[]
    for Rstud in parallel_layer:
        RvalueOfStud= Material_library[parallel_layer]
        Rtot=Rtot+RvalueOfStud
        Rvalue_loop.append(RvalueOfStud)
    print "this value of R for this layer is :" + str(Rvalue_loop)
    
    print"the total R value without insulation  is "+ str(Rtot) +" (W/m^2 DegC)"
   
    results = {"total R":Rtot, "All values of R":Rvalue_loop}

    return results
    
def wallcalculations_series(series_layer):
    Material_library= {"stucco_25mm":0.037,"facebrick_100mm":0.075,"Building paper":0.011,"insideSurface":0.12,"outsideSurfaceSummer":0.044,
    "outsideSurfaceWinter":0.03,"woodBevelLappedsliding_200mm":0.14,"woodFiberBoard_13mm":0.23,"gypsum_13mm":0.079,
    "glassFibreInsulation_25mm":2.52,"woodStud_90mm":0.63,"wood50mm":0.44, "Added_insulation":3.85}
    
    series_layer=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","glassFibreInsulation_25mm","woodStud_90mm",
    "gypsum_13mm","insideSurface", "Added_insulation" "wood50mm"]
    
    Rtot=0
    Rvalue_loop=[]
    for Rstud in series_layer:
        RvalueOfStud= Material_library[series_layer]
        Rtot=Rtot+RvalueOfStud
        Rvalue_loop.append(RvalueOfStud)
    print "this value of R for this layer is :" + str(Rvalue_loop)
    
    print"the total R value without insulation  is "+ str(Rtot) +" (W/m^2 DegC)"
   
    results = {"total R":Rtot, "All values of R":Rvalue_loop}

    return results
    
    