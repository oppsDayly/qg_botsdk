class EVENTS:
    MESSAGE_CREATE = ("AT_MESSAGE_CREATE", "MESSAGE_CREATE")
    DM_CREATE = ("DIRECT_MESSAGE_CREATE",)
    MESSAGE_DELETE = (
        "MESSAGE_DELETE",
        "PUBLIC_MESSAGE_DELETE",
        "DIRECT_MESSAGE_DELETE",
    )
    FORUM = (
        "FORUM_THREAD_CREATE",
        "FORUM_THREAD_UPDATE",
        "FORUM_THREAD_DELETE",
        "FORUM_POST_CREATE",
        "FORUM_POST_DELETE",
        "FORUM_REPLY_CREATE",
        "FORUM_REPLY_DELETE",
        "FORUM_PUBLISH_AUDIT_RESULT",
    )
    GUILD = ("GUILD_CREATE", "GUILD_UPDATE", "GUILD_DELETE")
    CHANNEL = ("CHANNEL_CREATE", "CHANNEL_UPDATE", "CHANNEL_DELETE")
    GUILD_MEMBER = ("GUILD_MEMBER_ADD", "GUILD_MEMBER_UPDATE", "GUILD_MEMBER_REMOVE")
    REACTION = ("MESSAGE_REACTION_ADD", "MESSAGE_REACTION_REMOVE")
    INTERACTION = ("INTERACTION_CREATE",)
    AUDIT = ("MESSAGE_AUDIT_PASS", "MESSAGE_AUDIT_REJECT")
    OPEN_FORUM = (
        "OPEN_FORUM_THREAD_CREATE",
        "OPEN_FORUM_THREAD_UPDATE",
        "OPEN_FORUM_THREAD_DELETE",
        "OPEN_FORUM_POST_CREATE",
        "OPEN_FORUM_POST_DELETE",
        "OPEN_FORUM_REPLY_CREATE",
        "OPEN_FORUM_REPLY_DELETE",
    )
    AUDIO = ("AUDIO_START", "AUDIO_FINISH", "AUDIO_ON_MIC", "AUDIO_OFF_MIC")
    ALC_MEMBER = (
        "AUDIO_OR_LIVE_CHANNEL_MEMBER_ENTER",
        "AUDIO_OR_LIVE_CHANNEL_MEMBER_EXIT",
    )
