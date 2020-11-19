from __future__ import division
from webthing import (Action, Property, MultipleThings, Thing, Value,
                      WebThingServer)
import logging
import time
import uuid
import json
from utils import setup_logging


setup_logging()
logger = logging.getLogger("tdtest")


"""
///////////////////////////////////////////////////////////////////////////////////
////   Wrapper for WebThing to enable custom serialize/deserialize operations  ////
///////////////////////////////////////////////////////////////////////////////////
"""
TD_IRI = "https://www.w3.org/2019/wot/td#Thing"


class ThingWrapper(Thing):
    def __init__(self, id_, title_, type_=TD_IRI, description_=''):
        super(ThingWrapper, self).__init__(id_=id_, title=title_, type_=type_, description=description_)

    def to_json_ld(self):
        pass

    def to_rdf(self):
        pass


"""
//////////////////////////
////   HUE_LAMP CODE  ////
//////////////////////////
"""

"""AVAILABLE ACTIONS"""


class OnAction(Action):
    def __init__(self, thing, input_):
        super(OnAction, self).__init__(uuid.uuid4().hex, thing, 'on', input_=input_)

    def perform_action(self):
        self.thing.set_property('on', True)
        logger.info('ToggleAction performed')


class OffAction(Action):
    def __init__(self, thing, input_):
        super(OffAction, self).__init__(uuid.uuid4().hex, thing, 'off', input_=input_)

    def perform_action(self):
        self.thing.set_property('on', False)
        logger.info('ToggleAction performed')


class ChangeColor(Action):
    def __init__(self, thing, input_):
        super(ChangeColor, self).__init__(uuid.uuid4().hex, thing, 'color', input_=input_)

    def perform_action(self):
        color = self.input['color']
        logger.info('Color changed to: ' + color)
        self.thing.set_property('color', color)


def make_hue_lamp_thing():
    thing_id = "urn:dev:test:007-WoTLamp-1"
    thing = ThingWrapper(id_=thing_id, title_="HueLampThing", type_=TD_IRI,
                         description_="Philips Hue Lamp in Lab 308")

    thing.add_property(
        Property(thing,
                 'on',
                 Value(False),
                 metadata={
                     '@type': 'OnOffProperty',
                     'title': 'On/Off',
                     'type': 'boolean',
                     'description': 'Whether the lamp is turned on',
                 }))

    thing.add_property(
        Property(thing,
                 'brightness',
                 Value(0),
                 metadata={
                     '@type': 'BrightnessProperty',
                     'title': 'Brightness',
                     'type': 'integer',
                     'description': 'The level of light from 0-100',
                     'minimum': 0,
                     'maximum': 100,
                     'unit': 'percent',
                 })
    )

    thing.add_property(
        Property(thing,
                 'color',
                 Value('white'),
                 metadata={
                     '@type': 'Color',
                     'title': 'Light color',
                     'type': 'string',
                     'description': 'Lamp Color',
                 }))

    # thing actions #
    thing.add_available_action('on',
                               {
                                   'title': 'OnAction',
                                   'description': 'Turn the lamp on',
                                   'metadata': {
                                       'input': {
                                           'type': 'None'
                                       }
                                   }
                               },
                               OnAction)

    thing.add_available_action('off',
                               {
                                   'title': 'OffAction',
                                   'description': 'Turn the lamp off',
                                   'metadata': {
                                       'input': {
                                           'type': 'None'
                                       }
                                   }
                               },
                               OffAction)

    thing.add_available_action('color',
                               {
                                   'title': 'ChangeColor',
                                   'description': 'Change hue_light color',
                                   'metadata': {
                                       'input': {
                                           'type': 'object',
                                           'required': ['color']
                                       }
                                   }
                               },
                               ChangeColor)
    return thing


"""
//////////////////////////
////    BLINDS CODE   ////
//////////////////////////
"""


class BlindsUp(Action):
    def __init__(self, thing, input_):
        super(BlindsUp, self).__init__(uuid.uuid4().hex, thing, 'blinds_up', input_=input_)

    def perform_action(self):
        time.sleep(1)
        logger.info('Se ridica jaluzelele')


class BlindsDown(Action):
    def __init__(self, thing, input_):
        super(BlindsDown, self).__init__(uuid.uuid4().hex, thing, 'blinds_down', input_=input_)

    def perform_action(self):
        time.sleep(1)
        logger.info('Se coboara jaluzelele')


class BlindsStop(Action):
    def __init__(self, thing, input_):
        super(BlindsStop, self).__init__(uuid.uuid4().hex, thing, 'blinds_stop', input_=input_)

    def perform_action(self):
        time.sleep(1)
        logger.info('Se opresc jaluzelele')


def set_blind_actions(thing: ThingWrapper):
    thing.add_available_action(
        'blinds_up',
        {
            'title': 'Blinds up',
            'description': 'Rise the blinds',
            'metadata': {
                'input': 'None'
            }
        },
        BlindsUp
    )

    thing.add_available_action(
        'blinds_down',
        {
            'title': 'Blinds down',
            'description': 'Lower the blinds',
            'metadata': {
                'input': 'None'
            }
        },
        BlindsDown
    )

    thing.add_available_action(
        'blinds_stop',
        {
            'title': 'Blinds stop',
            'description': 'Stop the blinds',
            'metadata': {
                'input': 'None'
            }
        },
        BlindsStop
    )

    return thing

def make_blinds1_thing():
    thing_id = "urn:dev:test:007-WoTBlinds-1"
    thing = ThingWrapper(id_=thing_id, title_="BlindsThing-1", type_=TD_IRI,
                         description_="South facing blinds in lab 308")
    thing = set_blind_actions(thing)

    return thing


def make_blinds2_thing():
    thing_id = "urn:dev:test:007-WoTBlinds-2"
    thing = ThingWrapper(id_=thing_id, title_="BlindsThing-2", type_=TD_IRI,
                         description_="East facing blinds in lab 308")
    thing = set_blind_actions(thing)

    return thing


def run_multiple_things_server():
    hue_lamp = make_hue_lamp_thing()
    blinds1 = make_blinds1_thing()
    blinds2 = make_blinds2_thing()
    things = [hue_lamp, blinds1, blinds2]

    server = WebThingServer(MultipleThings(things, 'AI-MAS LAB'), port=8888)

    try:
        logger.info('starting the server')
        server.start()

    except KeyboardInterrupt:
        logger.info('stopping the server')
        server.stop()
        logger.info('done')


if __name__ == '__main__':
    run_multiple_things_server()
