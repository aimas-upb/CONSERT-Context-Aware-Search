import connexion
import six

from openapi_server.models.lecture import Lecture  # noqa: E501
from openapi_server import util


def lectures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lecture

    Gets a list of all instances of Lecture (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Lecture) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lecture]
    """
    return 'do some magic!'


def lectures_thingid_get(thingid):  # noqa: E501
    """Get a single Lecture by its id

    Gets the details of a given Lecture (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Lecture) # noqa: E501

    :param thingid: The ID of the Lecture to be retrieved
    :type thingid: str

    :rtype: Lecture
    """
    return 'do some magic!'
