import connexion
import six
from owlready2 import *

from openapi_server.models.event import Event  # noqa: E501
from openapi_server import util


def events_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Event

    Gets a list of all instances of Event (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Event) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Event]
    """
    onto = get_ontology("precis-schedule-ont.owl").load()

    response = []
    for i in onto.Event.instances():
        iri = i.iri
        thingid = iri.split("#")[-1]
        response.append(
            Event(
                id=thingid,
                label=i.label
            )
        )

    return response


def events_thingid_get(thingid):  # noqa: E501
    """Get a single Event by its id

    Gets the details of a given Event (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Event) # noqa: E501

    :param thingid: The ID of the Event to be retrieved
    :type thingid: str

    :rtype: Event
    """


    onto = get_ontology("precis-schedule-ont.owl").load()
    instance = onto.search(iri="http://aimas.cs.pub.ro/robin/precis-schedule#" + thingid)

    if not instance:
        return {
            "error": True,
            "message": "Invalid id"
        }

    return Event(
        id=thingid,
        label=instance[0].label,
    )
