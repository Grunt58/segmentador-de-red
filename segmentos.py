import xlsxwriter

class Red_Segmentada:

    # Información de cada segmento de red
    data: list = []

    def __init__(self, file_name: str, sheet_name="segmentos") -> None:
        self.file_name = file_name
        self.sheet_name = sheet_name

    # Creamos el archivo de Excel (xlsx)
    def create_file(self) -> None:
        workbook = xlsxwriter.Workbook(f"{self.file_name}.xlsx")
        worksheet = workbook.add_worksheet(self.sheet_name)

    # Recopilación de información de cada segmento
    def add_segment(self, segment: list) -> None:
        self.data.append(segment)