from utilities import get_k_previous_date


class ReviewRule:
    past_array = [1, 2, 4, 7, 11, 16]

    @classmethod
    def get_reviewed_dates(cls):
        folder_names = []
        for num in cls.past_array:
            folder_names.append(get_k_previous_date(k=num))

        return folder_names

