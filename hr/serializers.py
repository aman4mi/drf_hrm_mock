from rest_framework import serializers
from .models import *

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields='__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields='__all__'

class OrganizationSerializers(serializers.ModelSerializer):        
    class Meta:
        model = Organization
        fields='__all__'

class OfficeTypeCountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = OfficeType
        fields='__all__'

class DomainStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = DomainStatus
        fields='__all__'

class OfficeAddressSerializers(serializers.ModelSerializer):        
    class Meta:
        model = OfficeAddress
        fields='__all__'  
 
class CountryOfficeHierarchySerializers(serializers.ModelSerializer):
    class Meta:
        model = CountryOfficeHierarchy
        fields='__all__'

class PhysicalOfficeInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalOfficeInfo
        fields='__all__'

class OperationTypeSerializers(serializers.ModelSerializer):        
    class Meta:
        model = OperationType
        fields='__all__'

class ProgramTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgramType
        fields='__all__'

class EntityCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = EntityCategory
        fields='__all__'

class ProgramInfoSerializers(serializers.ModelSerializer):        
    class Meta:
        model = ProgramInfo
        fields='__all__'            

class ProjectInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields='__all__'

class GradeSerializers(serializers.ModelSerializer):        
    class Meta:
        model = Grade
        fields='__all__'

class EmploymentTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmploymentType
        fields='__all__'

class EmployeeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields='__all__'

class EmployeeDesignationSerializers(serializers.ModelSerializer):        
    class Meta:
        model = EmployeeDesignation
        fields='__all__'                    

class EmployeeLevelSerializers(serializers.ModelSerializer):        
    class Meta:
        model = EmployeeLevel
        fields='__all__'

class SalutationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Salutation
        fields='__all__'

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields='__all__'

class UniteSerializers(serializers.ModelSerializer):        
    class Meta:
        model = Unite
        fields='__all__' 

class EmployeeCoreInfoSerializers(serializers.ModelSerializer):        
    class Meta:
        model = EmployeeCoreInfo
        fields='__all__'         