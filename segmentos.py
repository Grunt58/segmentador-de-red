import xlsxwriter

class Red_Segmentada:

    # Información de cada segmento de red
    data: list = []
    options = {
    "data": data,
    "columns": [
        {
            "header": "No.",
        },
        {
            "header": "Host solicitados",
        },
        {
            "header": "Host encontrados",
        },
        {
            "header": "Dirección de red",
        },
        {
            "header": "Máscara digital",
        },
        {
            "header": "Máscara decimal",
        },
        {
            "header": "Primera IP utilizable",
        },
        {
            "header": "Última IP utilizable",
        },
        {
            "header": "Dirección de BR",
        }
    ]
}

    def __init__(self, file_name: str, sheet_name="segmentos") -> None:
        self.file_name = file_name
        self.sheet_name = sheet_name

    # Creamos el archivo de Excel (xlsx)
    def create_file(self) -> None:
        self.workbook = xlsxwriter.Workbook(f"{self.file_name}.xlsx")
        self.worksheet = self.workbook.add_worksheet(self.sheet_name)

    # Recopilación de información de cada segmento
    def add_segment(self, segment: list) -> None:
        self.data.append(segment)

    # Creación de tabla con encabezados
    def create_table(self, base_IP: str) -> None:
        self.worksheet.set_column("B:J", 20)
        self.worksheet.write("D2", "Dirección base")
        self.worksheet.write("E2", base_IP)
        self.worksheet.insert_image("B2", "bits.png")
        self.worksheet.add_table("B6:J11", self.options)
        # Creación del
        self.workbook.close()