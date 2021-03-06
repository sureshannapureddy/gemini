# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class FeatureExtractorStub(object):
  """Feature Extractor Service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Identifiers = channel.unary_unary(
        '/tech.sourced.featurext.generated.FeatureExtractor/Identifiers',
        request_serializer=service__pb2.IdentifiersRequest.SerializeToString,
        response_deserializer=service__pb2.FeaturesReply.FromString,
        )
    self.Literals = channel.unary_unary(
        '/tech.sourced.featurext.generated.FeatureExtractor/Literals',
        request_serializer=service__pb2.LiteralsRequest.SerializeToString,
        response_deserializer=service__pb2.FeaturesReply.FromString,
        )
    self.Uast2seq = channel.unary_unary(
        '/tech.sourced.featurext.generated.FeatureExtractor/Uast2seq',
        request_serializer=service__pb2.Uast2seqRequest.SerializeToString,
        response_deserializer=service__pb2.FeaturesReply.FromString,
        )
    self.Graphlet = channel.unary_unary(
        '/tech.sourced.featurext.generated.FeatureExtractor/Graphlet',
        request_serializer=service__pb2.GraphletRequest.SerializeToString,
        response_deserializer=service__pb2.FeaturesReply.FromString,
        )


class FeatureExtractorServicer(object):
  """Feature Extractor Service
  """

  def Identifiers(self, request, context):
    """Extract identifiers weighted set
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Literals(self, request, context):
    """Extract literals weighted set
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Uast2seq(self, request, context):
    """Extract uast2seq weighted set
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Graphlet(self, request, context):
    """Extract graphlet weighted set
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeatureExtractorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Identifiers': grpc.unary_unary_rpc_method_handler(
          servicer.Identifiers,
          request_deserializer=service__pb2.IdentifiersRequest.FromString,
          response_serializer=service__pb2.FeaturesReply.SerializeToString,
      ),
      'Literals': grpc.unary_unary_rpc_method_handler(
          servicer.Literals,
          request_deserializer=service__pb2.LiteralsRequest.FromString,
          response_serializer=service__pb2.FeaturesReply.SerializeToString,
      ),
      'Uast2seq': grpc.unary_unary_rpc_method_handler(
          servicer.Uast2seq,
          request_deserializer=service__pb2.Uast2seqRequest.FromString,
          response_serializer=service__pb2.FeaturesReply.SerializeToString,
      ),
      'Graphlet': grpc.unary_unary_rpc_method_handler(
          servicer.Graphlet,
          request_deserializer=service__pb2.GraphletRequest.FromString,
          response_serializer=service__pb2.FeaturesReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tech.sourced.featurext.generated.FeatureExtractor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
