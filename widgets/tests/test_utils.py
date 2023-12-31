from django.test import TestCase
from widgets.utils import extract_app_from_model
from test_htmx_widgets.models import TestModel


class TestExtractAppFromModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        # This line creates a new database entry using the TempModel.
        cls.test_model = TestModel.objects.create(text="text", integer=1)

    def test_extract_app_from_model(self):
        obj = self.test_model
        output = extract_app_from_model(obj)
        expected_output = {
            'model_name': 'testmodel',
            'app_label': 'test_htmx_widgets',
            'pk': obj.pk
        }
        self.assertDictEqual(output, expected_output)
