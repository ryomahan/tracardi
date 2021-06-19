from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner


class UpdateProfileAction(ActionRunner):

    def __init__(self, *args, **kwargs):
        pass

    async def run(self, void):
        self.profile.metadata.updated = True
        print("meta", self.profile.metadata)
        return None


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='app.process_engine.action.v1.update_profile_action',
            className='UpdateProfileAction',
            inputs=["void"],
            outputs=[],
            init={},
            manual="update_profile_action"
        ),
        metadata=MetaData(
            name='Update profile',
            desc='Updates profile in storage.',
            type='flowNode',
            width=200,
            height=100,
            icon='store',
            group=["Customer Data"]
        )
    )
