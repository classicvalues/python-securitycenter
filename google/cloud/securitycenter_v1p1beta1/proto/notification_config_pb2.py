# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter_v1p1beta1/proto/notification_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/securitycenter_v1p1beta1/proto/notification_config.proto",
    package="google.cloud.securitycenter.v1p1beta1",
    syntax="proto3",
    serialized_options=b"\n)com.google.cloud.securitycenter.v1p1beta1P\001ZSgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1p1beta1;securitycenter\252\002%Google.Cloud.SecurityCenter.V1P1Beta1\312\002%Google\\Cloud\\SecurityCenter\\V1p1beta1\352\002(Google::Cloud::SecurityCenter::V1p1beta1\352A@\n\033pubsub.googleapis.com/Topic\022!projects/{project}/topics/{topic}",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nEgoogle/cloud/securitycenter_v1p1beta1/proto/notification_config.proto\x12%google.cloud.securitycenter.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb6\x04\n\x12NotificationConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12W\n\nevent_type\x18\x03 \x01(\x0e\x32\x43.google.cloud.securitycenter.v1p1beta1.NotificationConfig.EventType\x12\x36\n\x0cpubsub_topic\x18\x04 \x01(\tB \xfa\x41\x1d\n\x1bpubsub.googleapis.com/Topic\x12\x1c\n\x0fservice_account\x18\x05 \x01(\tB\x03\xe0\x41\x03\x12\x65\n\x10streaming_config\x18\x06 \x01(\x0b\x32I.google.cloud.securitycenter.v1p1beta1.NotificationConfig.StreamingConfigH\x00\x1a!\n\x0fStreamingConfig\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t"4\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x46INDING\x10\x01:}\xea\x41z\n0securitycenter.googleapis.com/NotificationConfig\x12\x46organizations/{organization}/notificationConfigs/{notification_config}B\x0f\n\rnotify_configB\xc0\x02\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZSgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1p1beta1;securitycenter\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1\xea\x41@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
    ],
)


_NOTIFICATIONCONFIG_EVENTTYPE = _descriptor.EnumDescriptor(
    name="EventType",
    full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.EventType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="EVENT_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FINDING",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=573,
    serialized_end=625,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONCONFIG_EVENTTYPE)


_NOTIFICATIONCONFIG_STREAMINGCONFIG = _descriptor.Descriptor(
    name="StreamingConfig",
    full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.StreamingConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.StreamingConfig.filter",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=538,
    serialized_end=571,
)

_NOTIFICATIONCONFIG = _descriptor.Descriptor(
    name="NotificationConfig",
    full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.description",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="event_type",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.event_type",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="pubsub_topic",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.pubsub_topic",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\372A\035\n\033pubsub.googleapis.com/Topic",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="service_account",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.service_account",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="streaming_config",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.streaming_config",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_NOTIFICATIONCONFIG_STREAMINGCONFIG,],
    enum_types=[_NOTIFICATIONCONFIG_EVENTTYPE,],
    serialized_options=b"\352Az\n0securitycenter.googleapis.com/NotificationConfig\022Forganizations/{organization}/notificationConfigs/{notification_config}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="notify_config",
            full_name="google.cloud.securitycenter.v1p1beta1.NotificationConfig.notify_config",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=203,
    serialized_end=769,
)

_NOTIFICATIONCONFIG_STREAMINGCONFIG.containing_type = _NOTIFICATIONCONFIG
_NOTIFICATIONCONFIG.fields_by_name[
    "event_type"
].enum_type = _NOTIFICATIONCONFIG_EVENTTYPE
_NOTIFICATIONCONFIG.fields_by_name[
    "streaming_config"
].message_type = _NOTIFICATIONCONFIG_STREAMINGCONFIG
_NOTIFICATIONCONFIG_EVENTTYPE.containing_type = _NOTIFICATIONCONFIG
_NOTIFICATIONCONFIG.oneofs_by_name["notify_config"].fields.append(
    _NOTIFICATIONCONFIG.fields_by_name["streaming_config"]
)
_NOTIFICATIONCONFIG.fields_by_name[
    "streaming_config"
].containing_oneof = _NOTIFICATIONCONFIG.oneofs_by_name["notify_config"]
DESCRIPTOR.message_types_by_name["NotificationConfig"] = _NOTIFICATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationConfig = _reflection.GeneratedProtocolMessageType(
    "NotificationConfig",
    (_message.Message,),
    {
        "StreamingConfig": _reflection.GeneratedProtocolMessageType(
            "StreamingConfig",
            (_message.Message,),
            {
                "DESCRIPTOR": _NOTIFICATIONCONFIG_STREAMINGCONFIG,
                "__module__": "google.cloud.securitycenter_v1p1beta1.proto.notification_config_pb2",
                "__doc__": """The config for streaming-based notifications, which send each event as
    soon as it is detected.
    Attributes:
        filter:
            Expression that defines the filter to apply across
            create/update events of assets or findings as specified by the
            event type. The expression is a list of zero or more
            restrictions combined via logical operators ``AND`` and
            ``OR``. Parentheses are supported, and ``OR`` has higher
            precedence than ``AND``.  Restrictions have the form ``<field>
            <operator> <value>`` and may have a ``-`` character in front
            of them to indicate negation. The fields map to those defined
            in the corresponding resource.  The supported operators are:
            -  ``=`` for all value types. -  ``>``, ``<``, ``>=``, ``<=``
            for integer values. -  ``:``, meaning substring matching, for
            strings.  The supported value types are:  -  string literals
            in quotes. -  integer literals without quotes. -  boolean
            literals ``true`` and ``false`` without quotes.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1p1beta1.NotificationConfig.StreamingConfig)
            },
        ),
        "DESCRIPTOR": _NOTIFICATIONCONFIG,
        "__module__": "google.cloud.securitycenter_v1p1beta1.proto.notification_config_pb2",
        "__doc__": """Security Command Center notification configs.  A notification config
  is a Security Command Center resource that contains the configuration
  to send notifications for create/update events of findings, assets and
  etc.
  Attributes:
      name:
          The relative resource name of this notification config. See: h
          ttps://cloud.google.com/apis/design/resource_names#relative_re
          source_name Example: “organizations/{organization_id}/notifica
          tionConfigs/notify_public_bucket”.
      description:
          The description of the notification config (max of 1024
          characters).
      event_type:
          The type of events the config is for, e.g. FINDING.
      pubsub_topic:
          The Pub/Sub topic to send notifications to. Its format is
          “projects/[project_id]/topics/[topic]”.
      service_account:
          Output only. The service account that needs
          “pubsub.topics.publish” permission to publish to the Pub/Sub
          topic.
      notify_config:
          The config for triggering notifications.
      streaming_config:
          The config for triggering streaming-based notifications.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1p1beta1.NotificationConfig)
    },
)
_sym_db.RegisterMessage(NotificationConfig)
_sym_db.RegisterMessage(NotificationConfig.StreamingConfig)


DESCRIPTOR._options = None
_NOTIFICATIONCONFIG.fields_by_name["pubsub_topic"]._options = None
_NOTIFICATIONCONFIG.fields_by_name["service_account"]._options = None
_NOTIFICATIONCONFIG._options = None
# @@protoc_insertion_point(module_scope)
