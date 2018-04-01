from collections import defaultdict
from typing import Any, Dict

import pytest

from zulipterminal.ui_tools.buttons import StreamButton


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """
    Forces all the tests to work offline.
    """
    monkeypatch.delattr("requests.sessions.Session.request")
# --------------- Controller Fixtures -----------------------------------------


@pytest.fixture
def stream_button(mocker, monkeypatch):
    """
    Mocked stream button.
    """
    button = StreamButton(
        properties=['PTEST', 205, '#bfd56f'],
        controller=mocker.patch('zulipterminal.core.Controller'),
        view=mocker.patch('zulipterminal.ui.View')
    )
    return button


# --------------- Model Fixtures ----------------------------------------------


@pytest.fixture(scope='module')
def messages_successful_response() -> Dict[str, Any]:
    """
    A successful response from a /messages API query.
    """
    response = {
        'anchor': 10000000000000000,
        'messages': [{
            'id': 537286,
            'sender_full_name': 'Foo Foo',
            'timestamp': 1520918722,
            'client': 'website',
            'recipient_id': 6076,
            'sender_email': 'foo@zulip.com',
            'type': 'stream',
            'sender_realm_str': '',
            'flags': ['read'],
            'sender_id': 5140,
            'content_type': 'text/x-markdown',
            'stream_id': 205,
            'subject': 'Test',
            'reactions': [],
            'subject_links': [],
            'avatar_url': '/user_avatars/2/foo.png?x=x&version=2',
            'is_me_message': False,
            'sender_short_name': 'foo',
            'content': 'Stream content here.',
            'display_recipient': 'PTEST',
            }, {
            'id': 537287,
            'sender_full_name': 'Foo Foo',
            'timestamp': 1520918736,
            'client': 'website',
            'recipient_id': 5780,
            'is_me_message': False,
            'sender_email': 'foo@zulip.com',
            'flags': ['read'],
            'sender_id': 5140,
            'content_type': 'text/x-markdown',
            'sender_realm_str': '',
            'subject': '',
            'reactions': [],
            'type': 'private',
            'avatar_url': '/user_avatars/2/foo.png?x=x&version=2',
            'subject_links': [],
            'sender_short_name': 'foo',
            'content': 'Hey PM content here.',
            'display_recipient': [{
                'id': 5179,
                'is_mirror_dummy': False,
                'full_name': 'Boo Boo',
                'short_name': 'boo',
                'email': 'boo@zulip.com',
                }, {
                'short_name': 'foo',
                'id': 5140,
                'is_mirror_dummy': False,
                'full_name': 'Foo Foo',
                'email': 'foo@zulip.com',
                }],
            }],
        'result': 'success',
        'msg': '',
    }
    return response


@pytest.fixture(scope="module")
def initial_data():
    """
    Response from /register API request.
    """
    return {
        'unsubscribed': [{
            'audible_notifications': False,
            'description': 'announce',
            'stream_id': 7,
            'is_old_stream': True,
            'desktop_notifications': False,
            'pin_to_top': False,
            'stream_weekly_traffic': 0,
            'invite_only': False,
            'name': 'announce',
            'push_notifications': False,
            'email_address': '',
            'color': '#bfd56f',
            'in_home_view': True
        }],
        'result': 'success',
        'queue_id': '1522420755:786',
        'realm_users': [{
            'bot_type': None,
            'is_bot': False,
            'is_admin': False,
            'email': 'tomasfariassantana@gmail.com',
            'full_name': 'Tomás Farías',
            'user_id': 5827,
            'avatar_url': None,
            'is_active': True
        }, {
            'full_name': 'Jari Winberg',
            'user_id': 6086,
            'avatar_url': None,
            'is_active': True
        }, {
            'bot_type': None,
            'is_bot': False,
            'is_admin': False,
            'email': 'cloudserver2@hotmail.de',
            'full_name': 'Test Account',
            'user_id': 6085,
            'is_active': True
        }],
        'subscriptions': [{
            'audible_notifications': False,
            'description': '',
            'stream_id': 86,
            'is_old_stream': True,
            'desktop_notifications': False,
            'pin_to_top': False,
            'stream_weekly_traffic': 0,
            'invite_only': False,
            'name': 'Django',
            'push_notifications': False,
            'email_address': '',
            'color': '#94c849',
            'in_home_view': True
        }, {
            'audible_notifications': False,
            'description': 'The Google Summer of Code',
            'stream_id': 14,
            'is_old_stream': True,
            'desktop_notifications': False,
            'pin_to_top': False,
            'stream_weekly_traffic': 53,
            'invite_only': False,
            'name': 'GSoC',
            'push_notifications': False,
            'email_address': '',
            'color': '#c2c2c2',
            'in_home_view': True
        }],
        'msg': '',
        'max_message_id': 552761,
        'never_subscribed': [{
            'invite_only': False,
            'description': 'Announcements from the Zulip GCI Mentors',
            'stream_id': 87,
            'name': 'GCI announce',
            'is_old_stream': True,
            'stream_weekly_traffic': 0
        }, {
            'invite_only': False,
            'description': 'General discussion',
            'stream_id': 74,
            'name': 'GCI general',
            'is_old_stream': True,
            'stream_weekly_traffic': 0
        }],
        'unread_msgs': {
            'pms': [],
            'count': 0,
            'mentions': [],
            'streams': [],
            'huddles': []
        },
        'presences': {
            'nyan.salmon+sns@gmail.com': {
                'ZulipElectron': {
                    'pushable': False,
                    'client': 'ZulipElectron',
                    'status': 'idle',
                    'timestamp': 1522484059
                },
                'ZulipMobile': {
                    'pushable': False,
                    'client': 'ZulipMobile',
                    'status': 'idle',
                    'timestamp': 1522384165
                },
                'aggregated': {
                    'timestamp': 1522484059,
                    'client': 'ZulipElectron',
                    'status': 'idle'
                }
            },
            'aero31aero@gmail.com': {
                'website': {
                    'pushable': True,
                    'client': 'website',
                    'status': 'active',
                    'timestamp': 1522458138
                },
                'ZulipMobile': {
                    'pushable': True,
                    'client': 'ZulipMobile',
                    'status': 'active',
                    'timestamp': 1522480103
                },
                'aggregated': {
                    'timestamp': 1522480103,
                    'client': 'ZulipMobile',
                    'status': 'active'
                }
            }
        },
        'last_event_id': -1
    }


@pytest.fixture(scope="module")
def index_all_messages():
    """
    Expected index of `initial_data` fixture when model.narrow = []
    """
    return {
        'pointer': defaultdict(set, {}),
        'private': defaultdict(set, {}),
        'all_messages':  {537286, 537287},
        'all_private': set(),
        'messages': defaultdict(dict, {
            537286: {
                'type': 'stream',
                'sender_realm_str': '',
                'is_me_message': False,
                'content': 'Stream content here.',
                'recipient_id': 6076,
                'avatar_url': '/user_avatars/2/foo.png?x=x&version=2',
                'client': 'website',
                'stream_id': 205,
                'subject_links': [],
                'content_type': 'text/x-markdown',
                'display_recipient': 'PTEST',
                'reactions': [],
                'sender_short_name': 'foo',
                'id': 537286,
                'flags': ['read'],
                'sender_email': 'foo@zulip.com',
                'timestamp': 1520918722,
                'subject': 'Test',
                'sender_id': 5140,
                'sender_full_name': 'Foo Foo'
            },
            537287: {
                'type': 'private',
                'sender_realm_str': '',
                'is_me_message': False,
                'content': 'Hey PM content here.',
                'recipient_id': 5780,
                'client': 'website',
                'subject': '',
                'avatar_url': '/user_avatars/2/foo.png?x=x&version=2',
                'content_type': 'text/x-markdown',
                'display_recipient': [{
                    'id': 5179,
                    'full_name': 'Boo Boo',
                    'email': 'boo@zulip.com',
                    'short_name': 'boo',
                    'is_mirror_dummy': False
                }, {
                    'id': 5140,
                    'full_name': 'Foo Foo',
                    'email': 'foo@zulip.com',
                    'short_name': 'foo',
                    'is_mirror_dummy': False
                }],
                'sender_short_name': 'foo',
                'id': 537287,
                'flags': ['read'],
                'sender_email': 'foo@zulip.com',
                'timestamp': 1520918736,
                'reactions': [],
                'sender_id': 5140,
                'sender_full_name': 'Foo Foo',
                'subject_links': []
            }
        }),
        'all_stream': defaultdict(set, {}),
        'stream': defaultdict(dict, {})
    }


@pytest.fixture(scope="module")
def index_stream():
    """
    Expected index of initial_data when model.narrow = [['stream', '7']]
    """
    return {
        'private': defaultdict(set, {}),
        'all_messages': set(),
        'all_private': {
            537287
        },
        'all_stream': defaultdict(set, {
            205: {
                537286
            }
        }),
        'stream': defaultdict(dict, {}),
        'pointer': defaultdict(set, {}),
        'messages': defaultdict(dict, {
            537286: {
                'is_me_message': False,
                'flags': ['read'],
                'content_type': 'text/x-markdown',
                'sender_realm_str': '',
                'timestamp': 1520918722,
                'type': 'stream',
                'sender_full_name': 'Foo Foo',
                'content': 'Stream content here.',
                'display_recipient': 'PTEST',
                'sender_id': 5140,
                'sender_email': 'foo@zulip.com',
                'sender_short_name': 'foo',
                'reactions': [],
                'client': 'website',
                'subject': 'Test',
                'avatar_url': '/user_avatars/2/foo.png?x=x&version=2',
                'recipient_id': 6076,
                'subject_links': [],
                'id': 537286,
                'stream_id': 205
            },
            537287: {
                'flags': ['read'],
                'content_type': 'text/x-markdown',
                'sender_realm_str': '',
                'timestamp': 1520918736,
                'type': 'private',
                'sender_full_name': 'Foo Foo',
                'content': 'Hey PM content here.',
                'display_recipient': [{
                    'email': 'boo@zulip.com',
                    'full_name': 'Boo Boo',
                    'short_name': 'boo',
                    'id': 5179,
                    'is_mirror_dummy': False
                }, {
                    'email': 'foo@zulip.com',
                    'full_name': 'Foo Foo',
                    'short_name': 'foo',
                    'id': 5140,
                    'is_mirror_dummy': False
                }],
                'sender_id': 5140,
                'sender_email': 'foo@zulip.com',
                'sender_short_name': 'foo',
                'reactions': [],
                'client': 'website',
                'subject': '',
                'avatar_url': '/user_avatars/2/foo.png?x=x&version=2',
                'recipient_id': 5780,
                'subject_links': [],
                'id': 537287,
                'is_me_message': False
            }
        })
    }