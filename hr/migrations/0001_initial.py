# Generated by Django 3.0.6 on 2020-08-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('name', models.TextField()),
                ('countryId', models.IntegerField()),
                ('description', models.TextField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('name', models.TextField()),
                ('code', models.TextField()),
                ('shortName', models.TextField()),
                ('shortCode', models.TextField()),
                ('callingCode', models.TextField()),
                ('hasOperation', models.BooleanField()),
                ('localCurrencyName', models.TextField()),
                ('foreignCurrencyName', models.TextField()),
                ('minimumDenomination', models.FloatField()),
                ('timeZone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CountryOfficeHierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('officeCode', models.TextField()),
                ('officeName', models.TextField()),
                ('description', models.TextField()),
                ('officeHierarchyLevel', models.IntegerField()),
                ('setupDate', models.DateTimeField()),
                ('effectiveDate', models.DateTimeField()),
                ('isChecked', models.TextField()),
                ('countryOfOffice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
                ('description', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DomainStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('statusName', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('categoryName', models.TextField()),
                ('description', models.TextField()),
                ('isApplicableInFO', models.TextField()),
                ('domainStatusId', models.TextField()),
                ('shortName', models.TextField()),
                ('categoryRefCode', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('approvalStatus', models.TextField()),
                ('assignedDate', models.DateTimeField()),
                ('contractStartDate', models.DateTimeField()),
                ('coreProgramId', models.BigIntegerField()),
                ('coreProjectId', models.BigIntegerField()),
                ('countryLevelId', models.BigIntegerField()),
                ('createdBy', models.BigIntegerField()),
                ('curCountryJoinDate', models.DateTimeField()),
                ('curJobStartDate', models.DateTimeField()),
                ('curJobStatusId', models.BigIntegerField()),
                ('curOfficeJoinDate', models.DateTimeField()),
                ('dateCreated', models.DateTimeField()),
                ('departmentId', models.BigIntegerField()),
                ('deputationEndDate', models.DateTimeField()),
                ('domainStatusId', models.BigIntegerField()),
                ('eDesignationId', models.BigIntegerField()),
                ('emailAddressVarchar', models.TextField()),
                ('empCategoryId', models.BigIntegerField()),
                ('employeeDob', models.DateTimeField()),
                ('employeeLevelId', models.BigIntegerField()),
                ('employeeStatusId', models.BigIntegerField()),
                ('expiryDate', models.DateTimeField()),
                ('fDesignationId', models.BigIntegerField()),
                ('firstNameVarchar', models.TextField()),
                ('genderId', models.BigIntegerField()),
                ('homeCountryId', models.BigIntegerField()),
                ('isExpatriate', models.BooleanField()),
                ('isOnDeputation', models.BooleanField()),
                ('joiningDate', models.DateTimeField()),
                ('lastNameVarchar', models.TextField()),
                ('lastUpdated', models.DateTimeField()),
                ('middleNameVarchar', models.TextField()),
                ('nickNameVarchar', models.TextField()),
                ('nomineeFormVarchar', models.TextField()),
                ('noticePeriod', models.BigIntegerField()),
                ('officeCountryId', models.BigIntegerField()),
                ('officeInfoId', models.BigIntegerField()),
                ('pinNoVarchar', models.TextField()),
                ('constraintUkEmployeeCoreInfoPinNo', models.IntegerField()),
                ('programTypeId', models.BigIntegerField()),
                ('provisionEndDate', models.DateTimeField()),
                ('recruitmentCountryId', models.BigIntegerField()),
                ('refPinVarchar', models.TextField()),
                ('salutationId', models.BigIntegerField()),
                ('supervisorId', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('workingHour', models.BigIntegerField()),
                ('sl', models.IntegerField()),
                ('mobileVarchar', models.TextField()),
                ('positionIdVarchar', models.TextField()),
                ('rollNo', models.TextField()),
                ('unitId', models.BigIntegerField()),
                ('previousEmpCoreInfoIdVarchar', models.TextField()),
                ('probationNoticePeriod', models.BigIntegerField()),
                ('employeeNameVarchar', models.TextField()),
                ('nationalIdNo', models.TextField()),
                ('currencyNameVarchar', models.TextField()),
                ('payGroupId', models.BigIntegerField()),
                ('slabId', models.BigIntegerField()),
                ('isIssuedLetter', models.BooleanField()),
                ('isAttendance', models.BooleanField()),
                ('isIncrement', models.BooleanField()),
                ('isLeave', models.BooleanField()),
                ('isPromotion', models.BooleanField()),
                ('joiningDateAsPa', models.DateTimeField()),
                ('smartNidNoVarchar', models.TextField()),
                ('emailVarchar', models.TextField()),
                ('isIssuedRetireLetter', models.BooleanField()),
                ('religionId', models.BigIntegerField()),
                ('oldEmployeeNameVarchar', models.TextField()),
                ('oldFirstNameVarchar', models.TextField()),
                ('oldSupervisorId', models.BigIntegerField()),
                ('recruitReqNoVarchar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('number', models.IntegerField()),
                ('level_no', models.IntegerField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
                ('description', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EntityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('entityName', models.TextField()),
                ('description', models.TextField()),
                ('domainStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DomainStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
                ('description', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficeAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('addressLine1', models.TextField()),
                ('addressLine2', models.TextField()),
                ('zipCode', models.TextField()),
                ('provinceInfoId', models.BigIntegerField()),
                ('divisionInfoId', models.BigIntegerField()),
                ('districtInfoId', models.BigIntegerField()),
                ('tehsilInfoId', models.BigIntegerField()),
                ('branchRefCode', models.BigIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.City')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DomainStatus')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('officeTypeCode', models.TextField()),
                ('officeTypeName', models.TextField()),
                ('hierarchyLevel', models.IntegerField()),
                ('description', models.TextField()),
                ('officeOpType', models.CharField(choices=[('IN', 'International'), ('LO', 'Local'), ('NO', 'None')], default='LO', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='OperationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('operationCode', models.TextField()),
                ('operationDescription', models.TextField()),
                ('isSyncData', models.SmallIntegerField()),
                ('oldId', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgramInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('programCode', models.TextField()),
                ('programRefCode', models.TextField()),
                ('programName', models.TextField()),
                ('programDescription', models.TextField()),
                ('hasFieldOffice', models.BooleanField()),
                ('setupDate', models.TextField()),
                ('effectiveDate', models.TextField()),
                ('domainStatusId', models.BigIntegerField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
                ('entityCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.EntityCategory')),
                ('operationType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.OperationType')),
            ],
        ),
        migrations.CreateModel(
            name='Salutation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
                ('description', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('proposalId', models.TextField()),
                ('projectCode', models.TextField()),
                ('projectRefCode', models.TextField()),
                ('projectName', models.TextField()),
                ('projectDescription', models.TextField()),
                ('projectShortCode', models.TextField()),
                ('projectSetupDate', models.DateTimeField()),
                ('projectEffectiveDate', models.DateTimeField()),
                ('projectStartDate', models.DateTimeField()),
                ('projectEndDate', models.DateTimeField()),
                ('bookClosing', models.BooleanField()),
                ('parentProjectInfoId', models.DateTimeField()),
                ('departmentId', models.BigIntegerField()),
                ('createdOn', models.DateTimeField()),
                ('updatedOn', models.DateTimeField()),
                ('isIndependent', models.BooleanField()),
                ('isOverhead', models.BooleanField()),
                ('hoType', models.TextField()),
                ('boType', models.TextField()),
                ('mfProjectRefCode', models.TextField()),
                ('isNgoBeuro', models.BooleanField()),
                ('beuroFromDate', models.DateTimeField()),
                ('beuroToDate', models.DateTimeField()),
                ('isTrendxProject', models.BooleanField()),
                ('isSmartCollection', models.BooleanField()),
                ('hasMfOperation', models.BooleanField()),
                ('projectStatus', models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive'), ('CL', 'Close')], default='AC', max_length=2)),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
                ('domainStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DomainStatus')),
                ('programInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.ProgramInfo')),
                ('projectCountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Country')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('typeName', models.TextField()),
                ('description', models.TextField()),
                ('isSyncData', models.SmallIntegerField()),
                ('oldId', models.BigIntegerField()),
                ('domainStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DomainStatus')),
            ],
        ),
        migrations.AddField(
            model_name='programinfo',
            name='programType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.ProgramType'),
        ),
        migrations.CreateModel(
            name='PhysicalOfficeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('officeCode', models.TextField()),
                ('officeRefCode', models.TextField()),
                ('officeName', models.TextField()),
                ('setupDate', models.DateTimeField()),
                ('effectiveDate', models.DateTimeField()),
                ('officeStatusId', models.BigIntegerField()),
                ('mobileNo', models.TextField()),
                ('isHrOffice', models.BooleanField()),
                ('isMfOffice', models.BooleanField()),
                ('isDevOffice', models.BooleanField()),
                ('isUpazilaAccountsOffice', models.BooleanField()),
                ('verifyTB', models.BooleanField()),
                ('verifyPortfolio', models.BooleanField()),
                ('verifySavings', models.BooleanField()),
                ('mfBranchId', models.TextField()),
                ('mfRefCode', models.TextField()),
                ('devRefCode', models.TextField()),
                ('hasOperation', models.BooleanField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
                ('businessAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_address', to='hr.OfficeAddress')),
                ('officeCountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Country')),
                ('officeHierarchy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CountryOfficeHierarchy')),
                ('officeType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.OfficeType')),
                ('parentOffice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_office', to='hr.PhysicalOfficeInfo')),
                ('registeredAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_address', to='hr.OfficeAddress')),
                ('reportingTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporting_to', to='hr.PhysicalOfficeInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('name', models.TextField()),
                ('title', models.TextField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('webUrl', models.TextField()),
                ('code', models.TextField()),
                ('email', models.TextField()),
                ('contactName', models.TextField()),
                ('contactSurname', models.TextField()),
                ('contactPhone', models.TextField()),
                ('isActive', models.BooleanField()),
                ('shortName', models.TextField()),
                ('isMainOrganization', models.BooleanField()),
                ('isProjectized', models.BooleanField()),
                ('organizationType', models.TextField()),
                ('state', models.TextField()),
                ('city', models.TextField()),
                ('contactPersonDesignation', models.TextField()),
                ('extraInformation', models.TextField()),
                ('organizationId', models.TextField()),
                ('logo', models.TextField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('createdOn', models.DateTimeField()),
                ('updatedOn', models.DateTimeField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Country')),
                ('parentOrganization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_organization', to='hr.Organization')),
                ('rootOrganization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_organization', to='hr.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BigIntegerField()),
                ('code', models.TextField()),
                ('shortName', models.TextField()),
                ('shortOrder', models.IntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('jobSummary', models.TextField()),
                ('jobResponsibility', models.TextField()),
                ('jobAuthority', models.TextField()),
                ('requiredSkillSet', models.TextField()),
                ('isApplicableInFO', models.BooleanField()),
                ('designationRefCode', models.TextField()),
                ('domainStatusId', models.BigIntegerField()),
                ('createdBy', models.BigIntegerField()),
                ('updatedBy', models.BigIntegerField()),
                ('dateCreated', models.DateTimeField()),
                ('lastUpdated', models.DateTimeField()),
                ('programType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.ProgramType')),
            ],
        ),
        migrations.AddField(
            model_name='countryofficehierarchy',
            name='countryOfficeHierarchyStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DomainStatus'),
        ),
        migrations.AddField(
            model_name='countryofficehierarchy',
            name='officeType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.OfficeType'),
        ),
    ]
