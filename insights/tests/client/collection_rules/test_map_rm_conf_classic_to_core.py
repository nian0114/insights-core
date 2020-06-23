from insights.client.config import InsightsConfig
from insights.client.collection_rules import InsightsUploadConf
from mock.mock import patch, Mock, call


@patch('insights.client.collection_rules.InsightsUploadConf.load_redaction_file', Mock(return_value={'test': 'test'}))
@patch('insights.client.collection_rules.InsightsUploadConf.get_rm_conf_old', Mock(return_value={'test': 'test'}))
@patch('insights.client.collection_rules.InsightsUploadConf.map_rm_conf_classic_to_core')
def test_called_when_core_collection_enabled(map_rm_conf_classic_to_core):
    '''
    Verify that the function is called from get_rm_conf when core_collect=True
    '''
    upload_conf = InsightsUploadConf(Mock(core_collect=True))
    upload_conf.get_rm_conf()
    map_rm_conf_classic_to_core.assert_called_once()


@patch('insights.client.collection_rules.InsightsUploadConf.load_redaction_file', Mock(return_value={'test': 'test'}))
@patch('insights.client.collection_rules.InsightsUploadConf.get_rm_conf_old', Mock(return_value={'test': 'test'}))
@patch('insights.client.collection_rules.InsightsUploadConf.map_rm_conf_classic_to_core')
def test_not_called_when_core_collection_disabled(map_rm_conf_classic_to_core):
    '''
    Verify that the function is not called from get_rm_conf when core_collect=False
    '''
    upload_conf = InsightsUploadConf(Mock(core_collect=False))
    upload_conf.get_rm_conf()
    map_rm_conf_classic_to_core.assert_not_called()
