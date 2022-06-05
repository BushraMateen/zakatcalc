from django.db import models


class ZakatTable(models.Model):
    Line = models.IntegerField()
    name = models.CharField(max_length = 500,null=True)
    category = models.CharField(max_length = 500, null=True)
    AmtVal = models.IntegerField(null=True)
    ZakatRate = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    

class ZakatDetails(models.Model):
    UserId = models.IntegerField()
    Year = models.IntegerField()
    ZakatRate =  models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_PersonalCash_Hand_Bank_AmtVal =models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_PersonalCash_Hand_Bank_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_TotalValueof_Gold_silver_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_TotalValueof_Gold_silver_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_TotalValueof_stocks_shares_bonds_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_TotalValueof_stocks_shares_bonds_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_TotalcashValueof_retirement_pansion_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_TotalcashValueof_retirement_pansion_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_Loans_tobe_recievable_AmtVal =  models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_Loans_tobe_recievable_ZakatDue  = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_Other_expecected_recievables_AmtVal =  models.DecimalField(max_digits=15, decimal_places=2, null=True)
    PW_Other_expecected_recievables_ZakatDue  = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_BusinessCash_Hand_Bank_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_BusinessCash_Hand_Bank_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Netvalueof_business_tradegoods_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Netvalueof_business_tradegoods_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Total_business_recievables_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Total_business_recievables_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_NetIncomefrom_business_exploitedassets_duringyear_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_NetIncomefrom_business_exploitedassets_duringyear_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Currentvalueof_held_realestateproperties_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Currentvalueof_held_realestateproperties_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Zakat_Total_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    BW_Zakat_Total_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    D_Outstanding_necessary_debts_AmtVal = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    D_Outstanding_necessary_debts_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    D_Zakat_paid_in_advance_duringYear_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    D_Total_Deductions_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    D_Remaining_Zakat_Due_ZakatDue = models.DecimalField(max_digits=15, decimal_places=2, null=True)






 