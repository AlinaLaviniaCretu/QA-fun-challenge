import xml.etree.ElementTree as ET
from shapely.geometry import Polygon
import sys


class GCP:
    def __init__(self):
        self.input_file = self.get_input_file()
        self.output_file = self.get_output_file()
        self.xml_object = self.__open_and_parse_input_file()

    @staticmethod
    def get_input_file() -> str:
        """Take the input file from terminal."""
        input_file = sys.argv[1]
        return input_file

    @staticmethod
    def get_output_file() -> str:
        """Take the output file from terminal."""
        output_file = sys.argv[2]
        return output_file

    def __open_and_parse_input_file(self):
        """Parse XML input document into element tree and return its root element"""
        print('Parsing the XML input file...')
        return ET.parse(self.input_file).getroot()

    def get_xml_info(self, tag: str, prop: str) -> list:
        """Find all matching subelements by tag name in document order.
        Return a list containing their attribute values.

        *tag* is a string having an element tag
        *prop* the attribute of the tag
        """
        info_list = list()
        for type_tag in self.xml_object.findall("inputs/{}".format(tag)):
            value = type_tag.get(prop)
            info_list.append(value)
        return info_list

    def get_gcp_ids(self) -> list:
        """Get all the GCP ids"""
        return self.get_xml_info("gcps/GCP", "id")

    def get_coordinates(self) -> list:
        """Get the x and y coordinates of all GCP points"""
        return [
            [float(type_tag.get("x")), float(type_tag.get("y"))]
            for type_tag in self.xml_object.findall("inputs/gcps/GCP")
        ]

    @staticmethod
    def compute_area(data: list) -> float:
        """Compute a crude approximation of the area covered by the GCPs"""
        print('Computing area ...')
        xs = [x[0] for x in data]
        ys = [x[1] for x in data]
        rectangle_coords = [
            (min(xs), min(ys)),
            (max(xs), min(ys)),
            (max(xs), max(ys)),
            (min(xs), max(ys)),
        ]
        return Polygon(rectangle_coords).area

    def get_gcp_from_images(self) -> list:
        """Get all the GCPs ids that appear in images."""
        return self.get_xml_info("images/image/imageGCP", "id")

    def create_and_fill_output(self, gcps: list, area: float, gcp_in_images: list):
        """Create the output file containing
             - the number of GCPs,
             - the area covered by them
             - for each of the GCPs in how many images it can be seen
        """
        print(f'Writing the data to the {self.output_file}...')
        with open(self.output_file, "w") as f:
            f.write(f"{str(len(gcps))}\n")
            f.write(f"{area}\n")
            for id in gcps:
                f.write(f"{id}: {gcp_in_images.count(id)}\n")



def main():
    gcp_object = GCP()
    gcp_ids = gcp_object.get_gcp_ids()
    area = gcp_object.compute_area(gcp_object.get_coordinates())
    gcps_from_img = gcp_object.get_gcp_from_images()
    gcp_object.create_and_fill_output(gcp_ids, area, gcps_from_img)
    print('Done!')


if __name__ == "__main__":
    main()