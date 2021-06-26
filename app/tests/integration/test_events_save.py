import pytest
from app.domain.entity import Entity
from app.domain.payload.event_payload import EventPayload
from app.domain.payload.tracker_payload import TrackerPayload
from app.domain.profile import Profile
from app.domain.session import Session


@pytest.mark.asyncio
async def test_save_events():
    tracker_payload = TrackerPayload(
        session=Entity(id="12345"),
        profile=Profile.new(),
        source=Entity(id="scope"),
        events=[
            EventPayload(
                type="click",
                properties={"btn": [1, 2, 3]},
                options={"save": True}
            ),
            EventPayload(
                type="click",
                properties={"btn": [3, 4, 5]},
                options={"save": True}
            )
        ]
    )
    events = tracker_payload.get_events(Session.new(), Profile.new())
    result = await events.bulk().save()
    assert result.saved == 2  # profile id must be form session

    for id in result.ids:
        entity = Entity(id=id)
        await entity.storage("event").delete()
