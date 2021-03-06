# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 08:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0001_initial'),
        ('indicators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tolatable',
            name='country',
            field=models.ManyToManyField(blank=True, to='workflow.Country'),
        ),
        migrations.AddField(
            model_name='tolatable',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='tolatable',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tolatable',
            name='workflowlevel1',
            field=models.ManyToManyField(blank=True, to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='strategicobjective',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Country'),
        ),
        migrations.AddField(
            model_name='strategicobjective',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='reportingperiod',
            name='frequency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.Frequency'),
        ),
        migrations.AddField(
            model_name='reportingperiod',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='periodictarget',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
        migrations.AddField(
            model_name='objective',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='level',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Country'),
        ),
        migrations.AddField(
            model_name='level',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='level',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='indicatortype',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='approval_submitted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicator_submitted_by', to='workflow.TolaUser'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approving_indicator', to='workflow.TolaUser'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='data_collection_frequency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_collection_frequency', to='indicators.Frequency', verbose_name=b'Frequency of Data Collection'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='disaggregation',
            field=models.ManyToManyField(blank=True, to='indicators.DisaggregationType'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='external_service_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.ExternalServiceRecord', verbose_name=b'External Service ID'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='indicator_type',
            field=models.ManyToManyField(blank=True, to='indicators.IndicatorType'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicators.Level'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='objectives',
            field=models.ManyToManyField(blank=True, related_name='obj_indicator', to='indicators.Objective', verbose_name=b'Objective'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='reporting_frequency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.Frequency', verbose_name=b'Frequency of Reporting'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Sector'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='strategic_objectives',
            field=models.ManyToManyField(blank=True, related_name='strat_indicator', to='indicators.StrategicObjective', verbose_name=b'Country Strategic Objective'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='sub_sector',
            field=models.ManyToManyField(blank=True, related_name='indicator_sub_sector', to='workflow.Sector'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='workflowlevel1',
            field=models.ManyToManyField(to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='approval_submitted_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.TolaUser'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='approved_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.TolaUser'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='data_collection_frequency',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.Frequency'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='external_service_record',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.ExternalServiceRecord'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='level',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.Level'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='reporting_frequency',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.Frequency'),
        ),
        migrations.AddField(
            model_name='historicalindicator',
            name='sector',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.Sector'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='approved_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.TolaUser'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='evidence',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.Documentation'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='indicator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.Indicator'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='periodic_target',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.PeriodicTarget'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='tola_table',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicators.TolaTable'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='workflowlevel2',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.WorkflowLevel2'),
        ),
        migrations.AddField(
            model_name='frequency',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='externalservicerecord',
            name='external_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.ExternalService'),
        ),
        migrations.AddField(
            model_name='externalservice',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='disaggregationvalue',
            name='disaggregation_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.DisaggregationLabel'),
        ),
        migrations.AddField(
            model_name='disaggregationtype',
            name='organization',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='disaggregationlabel',
            name='disaggregation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.DisaggregationType'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approving_data', to='workflow.TolaUser', verbose_name=b'Originated By'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='disaggregation_value',
            field=models.ManyToManyField(blank=True, to='indicators.DisaggregationValue'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='evidence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Documentation', verbose_name=b'Evidence Document or Link'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='periodic_target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.PeriodicTarget'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='site',
            field=models.ManyToManyField(blank=True, to='workflow.SiteProfile'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='tola_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.TolaTable'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i_workflowlevel1', to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='workflowlevel2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i_workflowlevel2', to='workflow.WorkflowLevel2', verbose_name=b'Project Initiation'),
        ),
    ]
