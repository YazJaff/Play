// VMware vRealize Orchestrator action sample
//
// Find all VMs with a specific property value in vRA
// 
// For vRO/VRA 7.0+
//
// Action Inputs:
// vcacHost - vCAC:VCACHost - vRA IaaS Host
// propertyName - string - the custom property name to find
// propertyValue - Any - the custom property value to find
//
// Return type: Array/vCAC:VirtualMachine - All vRA IaaS VMs that have a specific custom property value

var propertyEntities = findPropertyEntitiesWithNameValue(vcacHost.id, propertyName, propertyValue);

var vms = getVmsForPropertyEntities(propertyEntities);

System.log("VMs found with matching property " + propertyName + " = '" + propertyValue + "' count: " + vms.length);
return vms;



function findPropertyEntitiesWithNameValue(hostId, name, value) {
	var propertyEntities = findVmPropertyEntitiesWithName(hostId, name);
	var filteredPropertyEntities = new Array();
	
	// must loop to filter by property value, since readModelEntitiesByCustomFilter 
	for each (var propertyEntity in propertyEntities) {
		if (propertyEntity.getProperty("PropertyValue") == value) {
			filteredPropertyEntities.push(propertyEntity);
		}
	}
	
	return filteredPropertyEntities;
}

function findVmPropertyEntitiesWithName(hostId, name) {
	var modelName = "ManagementModelEntities.svc";
	var entitySetName = "VirtualMachineProperties";
	
	var filter = new Properties();
	filter.put("PropertyName", name);
	//filter.put("PropertyValue", value); //just pass 1 filter since readModelEntitiesByCustomFilter ignores all but last filter
	
	return vCACEntityManager.readModelEntitiesByCustomFilter(hostId, modelName, entitySetName, filter, null);
}

function getVmsForPropertyEntities(propertyEntities) {
	var vms = new Array();
	var vmEntities;
	var vm;
	for each (var propertyEntity in propertyEntities) {
		vmEntities = propertyEntity.getLink(vcacHost, "VirtualMachine");
		if (vmEntities && vmEntities.length != 0) {
			vm = vmEntities[0].getInventoryObject();
			vms.push(vm);
		}
	}
	
	return vms;
}