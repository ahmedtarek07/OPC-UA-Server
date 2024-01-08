from opcua import Server,ua
import time
#CreateanOPCUAserver
MyServer=Server()
#Setuptheserverendpoint
MyServer.set_endpoint("opc.tcp://192.168.1.7:4840")
#Setupthenamespace
uri="NameSpace"
node_id=MyServer.register_namespace(uri)#giveadifferentnamespaceindextoeveryobject

#createanobjectasfolderinobjectswhichhasarootasrefrence
obj1=MyServer.nodes.objects.add_object(f"ns={3};s=Motor1","Object1")#specifythenodeid
obj2=MyServer.nodes.objects.add_object(f"ns={4};s=motor2","object2")
#Createavariableasthetargetnode(MyVariable)




#Createvariablesforobject1
press1=obj1.add_variable(f"ns={3};s=pressure","pressure1",0.0,varianttype=ua.VariantType.Float)
press1.set_writable()
temp1=obj1.add_variable(node_id,"Temperature1",0.0,varianttype=ua.VariantType.Int16)
temp1.set_writable()

#Createvariablesforobject2
temp2=obj2.add_variable(f"ns={4};s=temperature","Temperature2",0.0,varianttype=ua.VariantType.Float)
temp2.set_writable()
press2=obj2.add_variable(node_id,"pressure2",0.0,varianttype=ua.VariantType.Int32)
press2.set_writable()

#Starttheserver
MyServer.start()

temp1.set_value(25.0)#SetaconstantvalueforTemperature
press1.set_value(1010.0)#SetaconstantvalueforPressure


temp2.set_value(100)#SetaconstantvalueforTemperature
press2.set_value(2000)#SetaconstantvalueforPressure


try:
    #Yourserverlogicgoeshere
    while True:
        #Updatevariableswithrandomvaluesoranyotherlogic
        temperature1=temp1.get_value()#getvalueforTemperature
        pressure1=press1.get_value()#getvalueforPressure

        #temperature2=temp2.get_value()#getvalueforTemperature
        pressure2=press2.get_value()#getvalueforPressure
        temperature2=temp2.get_data_value()
        print(f"temperature1={temperature1}",f"pressure1={pressure1}")
        print(f"temperature2={temperature2}",f"pressure2={pressure2}")
        time.sleep(2)
finally:
#Stoptheserveronexit
    MyServer.stop()