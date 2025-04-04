class TestModelRelatedFields:
    TEST_MODEL = "test_model"
    NAME = "name"

    DESCRIPTION = "description"
    IS_ACTIVE = "is_active"
    CREATED_AT = "created_at"
    NEW_FILED = "new_filed"
    @classmethod
    def get_field_name(cls, model, field):
        return model._meta.get_field(field).name