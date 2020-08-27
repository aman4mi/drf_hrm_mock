from django.db import models
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    class Meta:
        db_table = "country"
    version = models.BigIntegerField()
    name = models.TextField()
    code = models.TextField()
    shortName = models.TextField()
    shortCode = models.TextField()
    callingCode = models.TextField()
    hasOperation = models.BooleanField()
    localCurrencyName = models.TextField()
    foreignCurrencyName = models.TextField()
    minimumDenomination = models.FloatField()
    timeZone = models.TextField()

class City(models.Model):
    version = models.BigIntegerField()
    name = models.TextField()
    countryId = models.IntegerField()
    description = models.TextField()
    lastUpdated = models.DateTimeField()   

class Organization(models.Model):    
    version = models.BigIntegerField()
    name = models.TextField()
    title = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField()
    webUrl = models.TextField()
    code = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    email = models.TextField()
    contactName = models.TextField()
    contactSurname = models.TextField()
    contactPhone = models.TextField()
    isActive = models.BooleanField()
    rootOrganization = models.ForeignKey('self',null=True,blank=True, related_name='root_organization', on_delete=models.CASCADE)
    shortName = models.TextField()
    isMainOrganization = models.BooleanField()
    isProjectized = models.BooleanField()
    parentOrganization = models.ForeignKey('self',null=True,blank=True,related_name='parent_organization', on_delete=models.CASCADE)
    organizationType = models.TextField()
    state = models.TextField()
    city = models.TextField()
    contactPersonDesignation = models.TextField()
    extraInformation = models.TextField()
    organizationId = models.TextField()
    logo = models.TextField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()

class OfficeType(models.Model):   
    version = models.BigIntegerField()
    officeTypeCode = models.TextField()
    officeTypeName = models.TextField()
    hierarchyLevel = models.IntegerField()
    description = models.TextField()

    class OfficeOperationType(models.TextChoices):
        INTERNATIONAL = 'IN', _('International')
        LOCAL = 'LO', _('Local')
        NONE = 'NO', _('None')

    officeOpType = models.CharField(
        max_length=2,
        choices=OfficeOperationType.choices,
        default=OfficeOperationType.LOCAL,
    )

class DomainStatus(models.Model):
    version = models.BigIntegerField()
    statusName = models.TextField()
    description = models.TextField()   

class OfficeAddress(models.Model):
    version = models.BigIntegerField()
    addressLine1 = models.TextField()
    addressLine2 = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zipCode = models.TextField()
    status = models.ForeignKey(DomainStatus, on_delete=models.CASCADE)
    provinceInfoId = models.BigIntegerField()
    divisionInfoId = models.BigIntegerField()
    districtInfoId = models.BigIntegerField()
    tehsilInfoId = models.BigIntegerField()
    branchRefCode = models.BigIntegerField()      

class CountryOfficeHierarchy(models.Model):
    version = models.BigIntegerField()
    countryOfOffice = models.ForeignKey(Country, on_delete=models.CASCADE)
    officeType = models.ForeignKey(OfficeType, on_delete=models.CASCADE)
    officeCode = models.TextField()
    officeName = models.TextField()
    description = models.TextField()
    officeHierarchyLevel = models.IntegerField()
    setupDate = models.DateTimeField()
    effectiveDate = models.DateTimeField()
    countryOfficeHierarchyStatus = models.ForeignKey(DomainStatus, on_delete=models.CASCADE)
    isChecked = models.TextField() 

class PhysicalOfficeInfo(models.Model):
    version = models.BigIntegerField()
    officeCode = models.TextField() 
    officeRefCode = models.TextField() 
    officeName = models.TextField() 
    officeType = models.ForeignKey(OfficeType, on_delete=models.CASCADE)
    # areaType (Object, AreaType)  -- -------------not found  
    setupDate = models.DateTimeField()
    effectiveDate = models.DateTimeField()
    registeredAddress = models.ForeignKey(OfficeAddress, related_name='registered_address', on_delete=models.CASCADE)
    businessAddress = models.ForeignKey(OfficeAddress, related_name='business_address', on_delete=models.CASCADE)
    officeStatusId = models.BigIntegerField()
    officeCountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    parentOffice = models.ForeignKey('self',null=True,blank=True,related_name='parent_office',  on_delete=models.CASCADE)
    mobileNo = models.TextField() 
    isHrOffice = models.BooleanField() 
    isMfOffice = models.BooleanField()
    isDevOffice = models.BooleanField()
    isUpazilaAccountsOffice = models.BooleanField() 
    verifyTB = models.BooleanField()
    verifyPortfolio = models.BooleanField()
    verifySavings = models.BooleanField()
    officeHierarchy = models.ForeignKey(CountryOfficeHierarchy, on_delete=models.CASCADE)
    reportingTo = models.ForeignKey('self', null=True, blank=True, related_name='reporting_to', on_delete=models.CASCADE)
    mfBranchId = models.TextField() 
    mfRefCode = models.TextField() 
    devRefCode = models.TextField()  
    hasOperation = models.BooleanField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField()
    lastUpdated = models.DateTimeField()  

class  OperationType(models.Model):
    version = models.BigIntegerField()
    operationCode = models.TextField() 
    operationDescription = models.TextField() 
    isSyncData = models.SmallIntegerField()
    oldId = models.BigIntegerField()
	 
class ProgramType(models.Model):
    version = models.BigIntegerField()
    typeName = models.TextField()    
    description = models.TextField() 
    domainStatus = models.ForeignKey(DomainStatus, on_delete=models.CASCADE)
    isSyncData = models.SmallIntegerField()
    oldId = models.BigIntegerField()

class EntityCategory(models.Model):
    version = models.BigIntegerField()
    entityName = models.TextField()     
    description = models.TextField()  
    domainStatus = models.ForeignKey(DomainStatus, on_delete=models.CASCADE)

class ProgramInfo(models.Model):
    version = models.BigIntegerField()
    programCode = models.TextField()  
    programRefCode = models.TextField()  
    programName = models.TextField()  
    programDescription = models.TextField()  
    operationType = models.ForeignKey(OperationType, on_delete=models.CASCADE)
    programType = models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    entityCategory = models.ForeignKey(EntityCategory, on_delete=models.CASCADE)
    hasFieldOffice = models.BooleanField()
    setupDate = models.TextField()  
    effectiveDate = models.TextField()  
    domainStatusId = models.BigIntegerField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField() 
    lastUpdated = models.DateTimeField()   

class ProjectInfo(models.Model):
    version = models.BigIntegerField()
    proposalId = models.TextField()
    projectCountry  = models.ForeignKey(Country, on_delete=models.CASCADE)
    projectCode = models.TextField()
    projectRefCode = models.TextField()
    projectName = models.TextField()
    projectDescription = models.TextField()
    projectShortCode = models.TextField()
    projectSetupDate = models.DateTimeField()
    projectEffectiveDate = models.DateTimeField()
    projectStartDate = models.DateTimeField()
    projectEndDate = models.DateTimeField()
    domainStatus = models.ForeignKey(DomainStatus, on_delete=models.CASCADE)
    programInfo  = models.ForeignKey(ProgramInfo, on_delete=models.CASCADE)
    bookClosing = models.BooleanField()
    parentProjectInfoId = models.DateTimeField()
    departmentId = models.BigIntegerField()   
    createdBy = models.IntegerField()
    updatedBy = models.IntegerField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()
    isIndependent = models.BooleanField()
    isOverhead = models.BooleanField()
    hoType = models.TextField()
    boType = models.TextField()
    mfProjectRefCode = models.TextField()
    isNgoBeuro = models.BooleanField()
    beuroFromDate = models.DateTimeField()
    beuroToDate = models.DateTimeField()
    isTrendxProject = models.BooleanField()
    isSmartCollection = models.BooleanField()
    hasMfOperation = models.BooleanField()

    class ProjectStatusCode(models.TextChoices):
        ACTIVE = 'AC', _('Active')
        INACTIVE = 'IN', _('Inactive')
        CLOSE = 'CL', _('Close')

    projectStatus = models.CharField(
        max_length=2,
        choices=ProjectStatusCode.choices,
        default=ProjectStatusCode.ACTIVE,
    )

    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField()
    lastUpdated = models.DateTimeField()    

class Grade(models.Model):       
    name =  models.TextField()
    code =  models.TextField()
    description = models.TextField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField()
    lastUpdated = models.DateTimeField() 


class EmploymentType(models.Model):  
    name=  models.TextField()
    code=  models.TextField()
    description=  models.TextField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField()
    lastUpdated = models.DateTimeField() 


class EmployeeCategory(models.Model):  
     version  = models.BigIntegerField()
     categoryName  =  models.TextField() 
     description  =  models.TextField()
     isApplicableInFO  =  models.TextField() 
     domainStatusId  =  models.TextField()
     shortName  =  models.TextField()
     categoryRefCode  =  models.TextField()
     createdBy = models.BigIntegerField()
     updatedBy = models.BigIntegerField()
     dateCreated = models.DateTimeField()
     lastUpdated = models.DateTimeField() 


class EmployeeDesignation(models.Model):  
     version  = models.BigIntegerField()
     code  =  models.TextField()
     shortName =  models.TextField()
     shortOrder = models.IntegerField()
     name =  models.TextField()
     description =  models.TextField()
     jobSummary =  models.TextField()
     jobResponsibility =  models.TextField()
     jobAuthority =  models.TextField()
     requiredSkillSet =  models.TextField()
     programType = models.ForeignKey(ProgramType, on_delete=models.CASCADE)    
     isApplicableInFO  = models.BooleanField() 
     designationRefCode  =  models.TextField()
     domainStatusId  = models.BigIntegerField()
     createdBy = models.BigIntegerField()
     updatedBy = models.BigIntegerField()
     dateCreated = models.DateTimeField()
     lastUpdated = models.DateTimeField() 


class EmployeeLevel(models.Model):  
     version  = models.BigIntegerField()
     name  =  models.TextField()
     description  =  models.TextField()
     number  = models.IntegerField()
     level_no  = models.IntegerField()
     createdBy = models.BigIntegerField()
     updatedBy = models.BigIntegerField()
     dateCreated = models.DateTimeField()
     lastUpdated = models.DateTimeField() 


class Salutation(models.Model):  
     version  = models.BigIntegerField()
     name =  models.TextField()
     description =  models.TextField()
     createdBy = models.BigIntegerField()
     updatedBy = models.BigIntegerField()
     dateCreated = models.DateTimeField()
     lastUpdated = models.DateTimeField() 


class Department(models.Model):      
    name =  models.TextField()
    code =  models.TextField()
    description =  models.TextField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField()
    lastUpdated = models.DateTimeField() 

class Unite(models.Model):        
    name =  models.TextField()
    code =  models.TextField()
    description =  models.TextField()
    createdBy = models.BigIntegerField()
    updatedBy = models.BigIntegerField()
    dateCreated = models.DateTimeField()
    lastUpdated = models.DateTimeField() 
	 
class EmployeeCoreInfo(models.Model):
     version = models.BigIntegerField()
     approvalStatus = models.TextField()
     assignedDate = models.DateTimeField()  
     contractStartDate = models.DateTimeField()  
     coreProgramId = models.BigIntegerField()
     coreProjectId = models.BigIntegerField()
     countryLevelId = models.BigIntegerField()
     createdBy = models.BigIntegerField()
     curCountryJoinDate = models.DateTimeField()  
     curJobStartDate = models.DateTimeField()  
     curJobStatusId = models.BigIntegerField()
     curOfficeJoinDate = models.DateTimeField()  
     dateCreated = models.DateTimeField()  
     departmentId = models.BigIntegerField()
     deputationEndDate = models.DateTimeField()  
     domainStatusId = models.BigIntegerField()
     eDesignationId = models.BigIntegerField()
     emailAddressVarchar = models.TextField()
     empCategoryId = models.BigIntegerField()
     employeeDob = models.DateTimeField()  
     employeeLevelId = models.BigIntegerField()
     employeeStatusId = models.BigIntegerField()
     expiryDate = models.DateTimeField()  
     fDesignationId = models.BigIntegerField()
     firstNameVarchar = models.TextField()
     genderId = models.BigIntegerField()
     homeCountryId = models.BigIntegerField()
     isExpatriate = models.BooleanField()
     isOnDeputation = models.BooleanField()
     joiningDate = models.DateTimeField()  
     lastNameVarchar = models.TextField()
     lastUpdated = models.DateTimeField()  
     middleNameVarchar = models.TextField()
     nickNameVarchar = models.TextField()
     nomineeFormVarchar = models.TextField()
     noticePeriod = models.BigIntegerField()
     officeCountryId = models.BigIntegerField()
     officeInfoId = models.BigIntegerField()
     pinNoVarchar = models.TextField()
     constraintUkEmployeeCoreInfoPinNo = models.IntegerField()
     programTypeId = models.BigIntegerField()
     provisionEndDate = models.DateTimeField()  
     recruitmentCountryId = models.BigIntegerField()
     refPinVarchar = models.TextField()
     salutationId = models.BigIntegerField()
     supervisorId = models.BigIntegerField()
     updatedBy = models.BigIntegerField()
     workingHour = models.BigIntegerField()
     sl = models.IntegerField()
     mobileVarchar = models.TextField()
     positionIdVarchar = models.TextField()
     rollNo = models.TextField()
     unitId = models.BigIntegerField()
     previousEmpCoreInfoIdVarchar = models.TextField()
     probationNoticePeriod = models.BigIntegerField()
     employeeNameVarchar = models.TextField()
     nationalIdNo = models.TextField()
     currencyNameVarchar = models.TextField()
     payGroupId = models.BigIntegerField()
     slabId = models.BigIntegerField()
     isIssuedLetter = models.BooleanField()
     isAttendance = models.BooleanField()
     isIncrement = models.BooleanField()
     isLeave = models.BooleanField()
     isPromotion = models.BooleanField()
     joiningDateAsPa = models.DateTimeField()  
     smartNidNoVarchar = models.TextField()
     emailVarchar = models.TextField()
     isIssuedRetireLetter = models.BooleanField()
     religionId = models.BigIntegerField()
     oldEmployeeNameVarchar = models.TextField()
     oldFirstNameVarchar = models.TextField()
     oldSupervisorId = models.BigIntegerField()
     recruitReqNoVarchar = models.TextField()	      