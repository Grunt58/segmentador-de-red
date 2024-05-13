import xlsxwriter

from resources import colors

text: object = colors.TextColors

class Red_Segmentada:

    # Información de cada segmento de red
    

    def __init__(self, file_name: str) -> None:
        self.base_IP: str = None
        self.file_name: str = file_name
        self.data: list = []
        self.options: dict = {
        "data": self.data,
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
                "header": "Máscara wildcard"
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
    
    def set_base_IP(self, base_IP: str) -> None:
        self.base_IP = base_IP

    # Creamos el archivo de Excel (xlsx)
    def create_file(self) -> None:
        self.workbook = xlsxwriter.Workbook(f"{self.file_name}.xlsx")

    # Recopilación de información de cada segmento
    def add_segment(self, segment: list) -> None:
        self.data.append(segment)

    # Creación de tabla con encabezados
    def create_table(self, index: int, sheet_name: str) -> None:
        self.worksheet = self.workbook.add_worksheet(sheet_name)
        self.worksheet.set_column("B:K", 20)
        self.worksheet.write("D2", "Dirección base")
        self.worksheet.write("E2", self.base_IP)
        self.worksheet.insert_image("B2", "bits.png")
        # 'index' sirve para saber la longitud de la tabla
        self.worksheet.add_table(f"B6:K{6 + index}", self.options)
        self.data.clear()

    def close_file(self) -> None:
        # Al cerrar, se crea el archivo
        while True:
            try:
                self.workbook.close()
            except xlsxwriter.exceptions.FileCreateError as err:
                input(f"{text.red}[{err}]: Cierra el archivo antes de continuar...{text.reset}")
                continue
            break