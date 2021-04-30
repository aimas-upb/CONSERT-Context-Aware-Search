import connexion
import six

from openapi_server.models.room import Room  # noqa: E501
from openapi_server import util


def rooms_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Room

    Gets a list of all instances of Room (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Room) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Room]
    """
    return 'do some magic!'


def rooms_thingid_get(thingid):  # noqa: E501
    """Get a single Room by its id

    Gets the details of a given Room (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Room) # noqa: E501

    :param thingid: The ID of the Room to be retrieved
    :type thingid: str

    :rtype: Room
    """
    return 'do some magic!'
