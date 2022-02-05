from Enums import *


class TestEnumHelpers:

    """ Ensuring the property_as_string_list returns the desired values """
    def test_string_list_are_strings(self):
        key_list = ChestMovements.property_as_string_list(Helpers.KEY)
        val_list = ChestMovements.property_as_string_list(Helpers.VALUE)
        assert 'DB_FLY' in key_list
        assert 'db fly' in val_list

    """ Ensuring all returned Enum values are present """
    def test_all_enums_return_lists(self):
        enums: list[EnumWithHelpers] = [
            VolumeEnums, 
            ChestMovements, 
            BicepMovements, 
            TricepMovements, 
            ShoulderMovements,
            BackMovements, 
            CoreMovements, 
            QuadMovements, 
            HamMovements, 
            CalfMovements
        ]

        for e in enums:
            assert len(e.property_as_string_list(Helpers.VALUE)) == len(e.__members__.values())
