import connexion
import six

from openapi_server.models.talk import Talk  # noqa: E501
from openapi_server import util


def talks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Talk

    Gets a list of all instances of Talk (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Talk) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Talk]
    """
    return 'do some magic!'


def talks_thingid_get(thingid):  # noqa: E501
    """Get a single Talk by its id

    Gets the details of a given Talk (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Talk) # noqa: E501

    :param thingid: The ID of the Talk to be retrieved
    :type thingid: str

    :rtype: Talk
    """
    return 'do some magic!'
