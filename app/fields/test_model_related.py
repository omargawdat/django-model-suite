class TestModelRelatedFields:
    TEST_MODEL = "test_model"
    NAME = "name"

    @classmethod
    def get_field_name(cls, model, field):
        return model._meta.get_field(field).name