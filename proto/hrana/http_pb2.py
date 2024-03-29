# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hrana.http.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import hrana_pb2 as hrana__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10hrana.http.proto\x12\nhrana.http\x1a\x0bhrana.proto\"\\\n\x0fPipelineReqBody\x12\x12\n\x05\x62\x61ton\x18\x01 \x01(\tH\x00\x88\x01\x01\x12+\n\x08requests\x18\x02 \x03(\x0b\x32\x19.hrana.http.StreamRequestB\x08\n\x06_baton\"\x7f\n\x10PipelineRespBody\x12\x12\n\x05\x62\x61ton\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x62\x61se_url\x18\x02 \x01(\tH\x01\x88\x01\x01\x12)\n\x07results\x18\x03 \x03(\x0b\x32\x18.hrana.http.StreamResultB\x08\n\x06_batonB\x0b\n\t_base_url\"a\n\x0cStreamResult\x12(\n\x02ok\x18\x01 \x01(\x0b\x32\x1a.hrana.http.StreamResponseH\x00\x12\x1d\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0c.hrana.ErrorH\x00\x42\x08\n\x06result\"J\n\rCursorReqBody\x12\x12\n\x05\x62\x61ton\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x05\x62\x61tch\x18\x02 \x01(\x0b\x32\x0c.hrana.BatchB\x08\n\x06_baton\"R\n\x0e\x43ursorRespBody\x12\x12\n\x05\x62\x61ton\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x62\x61se_url\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_batonB\x0b\n\t_base_url\"\xb1\x03\n\rStreamRequest\x12+\n\x05\x63lose\x18\x01 \x01(\x0b\x32\x1a.hrana.http.CloseStreamReqH\x00\x12/\n\x07\x65xecute\x18\x02 \x01(\x0b\x32\x1c.hrana.http.ExecuteStreamReqH\x00\x12+\n\x05\x62\x61tch\x18\x03 \x01(\x0b\x32\x1a.hrana.http.BatchStreamReqH\x00\x12\x31\n\x08sequence\x18\x04 \x01(\x0b\x32\x1d.hrana.http.SequenceStreamReqH\x00\x12\x31\n\x08\x64\x65scribe\x18\x05 \x01(\x0b\x32\x1d.hrana.http.DescribeStreamReqH\x00\x12\x32\n\tstore_sql\x18\x06 \x01(\x0b\x32\x1d.hrana.http.StoreSqlStreamReqH\x00\x12\x32\n\tclose_sql\x18\x07 \x01(\x0b\x32\x1d.hrana.http.CloseSqlStreamReqH\x00\x12<\n\x0eget_autocommit\x18\x08 \x01(\x0b\x32\".hrana.http.GetAutocommitStreamReqH\x00\x42\t\n\x07request\"\xbb\x03\n\x0eStreamResponse\x12,\n\x05\x63lose\x18\x01 \x01(\x0b\x32\x1b.hrana.http.CloseStreamRespH\x00\x12\x30\n\x07\x65xecute\x18\x02 \x01(\x0b\x32\x1d.hrana.http.ExecuteStreamRespH\x00\x12,\n\x05\x62\x61tch\x18\x03 \x01(\x0b\x32\x1b.hrana.http.BatchStreamRespH\x00\x12\x32\n\x08sequence\x18\x04 \x01(\x0b\x32\x1e.hrana.http.SequenceStreamRespH\x00\x12\x32\n\x08\x64\x65scribe\x18\x05 \x01(\x0b\x32\x1e.hrana.http.DescribeStreamRespH\x00\x12\x33\n\tstore_sql\x18\x06 \x01(\x0b\x32\x1e.hrana.http.StoreSqlStreamRespH\x00\x12\x33\n\tclose_sql\x18\x07 \x01(\x0b\x32\x1e.hrana.http.CloseSqlStreamRespH\x00\x12=\n\x0eget_autocommit\x18\x08 \x01(\x0b\x32#.hrana.http.GetAutocommitStreamRespH\x00\x42\n\n\x08response\"\x10\n\x0e\x43loseStreamReq\"\x11\n\x0f\x43loseStreamResp\"-\n\x10\x45xecuteStreamReq\x12\x19\n\x04stmt\x18\x01 \x01(\x0b\x32\x0b.hrana.Stmt\"6\n\x11\x45xecuteStreamResp\x12!\n\x06result\x18\x01 \x01(\x0b\x32\x11.hrana.StmtResult\"-\n\x0e\x42\x61tchStreamReq\x12\x1b\n\x05\x62\x61tch\x18\x01 \x01(\x0b\x32\x0c.hrana.Batch\"5\n\x0f\x42\x61tchStreamResp\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\x12.hrana.BatchResult\"M\n\x11SequenceStreamReq\x12\x10\n\x03sql\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06sql_id\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x06\n\x04_sqlB\t\n\x07_sql_id\"\x14\n\x12SequenceStreamResp\"M\n\x11\x44\x65scribeStreamReq\x12\x10\n\x03sql\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06sql_id\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x06\n\x04_sqlB\t\n\x07_sql_id\";\n\x12\x44\x65scribeStreamResp\x12%\n\x06result\x18\x01 \x01(\x0b\x32\x15.hrana.DescribeResult\"0\n\x11StoreSqlStreamReq\x12\x0e\n\x06sql_id\x18\x01 \x01(\x05\x12\x0b\n\x03sql\x18\x02 \x01(\t\"\x14\n\x12StoreSqlStreamResp\"#\n\x11\x43loseSqlStreamReq\x12\x0e\n\x06sql_id\x18\x01 \x01(\x05\"\x14\n\x12\x43loseSqlStreamResp\"\x18\n\x16GetAutocommitStreamReq\"0\n\x17GetAutocommitStreamResp\x12\x15\n\ris_autocommit\x18\x01 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hrana.http_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PIPELINEREQBODY']._serialized_start=45
  _globals['_PIPELINEREQBODY']._serialized_end=137
  _globals['_PIPELINERESPBODY']._serialized_start=139
  _globals['_PIPELINERESPBODY']._serialized_end=266
  _globals['_STREAMRESULT']._serialized_start=268
  _globals['_STREAMRESULT']._serialized_end=365
  _globals['_CURSORREQBODY']._serialized_start=367
  _globals['_CURSORREQBODY']._serialized_end=441
  _globals['_CURSORRESPBODY']._serialized_start=443
  _globals['_CURSORRESPBODY']._serialized_end=525
  _globals['_STREAMREQUEST']._serialized_start=528
  _globals['_STREAMREQUEST']._serialized_end=961
  _globals['_STREAMRESPONSE']._serialized_start=964
  _globals['_STREAMRESPONSE']._serialized_end=1407
  _globals['_CLOSESTREAMREQ']._serialized_start=1409
  _globals['_CLOSESTREAMREQ']._serialized_end=1425
  _globals['_CLOSESTREAMRESP']._serialized_start=1427
  _globals['_CLOSESTREAMRESP']._serialized_end=1444
  _globals['_EXECUTESTREAMREQ']._serialized_start=1446
  _globals['_EXECUTESTREAMREQ']._serialized_end=1491
  _globals['_EXECUTESTREAMRESP']._serialized_start=1493
  _globals['_EXECUTESTREAMRESP']._serialized_end=1547
  _globals['_BATCHSTREAMREQ']._serialized_start=1549
  _globals['_BATCHSTREAMREQ']._serialized_end=1594
  _globals['_BATCHSTREAMRESP']._serialized_start=1596
  _globals['_BATCHSTREAMRESP']._serialized_end=1649
  _globals['_SEQUENCESTREAMREQ']._serialized_start=1651
  _globals['_SEQUENCESTREAMREQ']._serialized_end=1728
  _globals['_SEQUENCESTREAMRESP']._serialized_start=1730
  _globals['_SEQUENCESTREAMRESP']._serialized_end=1750
  _globals['_DESCRIBESTREAMREQ']._serialized_start=1752
  _globals['_DESCRIBESTREAMREQ']._serialized_end=1829
  _globals['_DESCRIBESTREAMRESP']._serialized_start=1831
  _globals['_DESCRIBESTREAMRESP']._serialized_end=1890
  _globals['_STORESQLSTREAMREQ']._serialized_start=1892
  _globals['_STORESQLSTREAMREQ']._serialized_end=1940
  _globals['_STORESQLSTREAMRESP']._serialized_start=1942
  _globals['_STORESQLSTREAMRESP']._serialized_end=1962
  _globals['_CLOSESQLSTREAMREQ']._serialized_start=1964
  _globals['_CLOSESQLSTREAMREQ']._serialized_end=1999
  _globals['_CLOSESQLSTREAMRESP']._serialized_start=2001
  _globals['_CLOSESQLSTREAMRESP']._serialized_end=2021
  _globals['_GETAUTOCOMMITSTREAMREQ']._serialized_start=2023
  _globals['_GETAUTOCOMMITSTREAMREQ']._serialized_end=2047
  _globals['_GETAUTOCOMMITSTREAMRESP']._serialized_start=2049
  _globals['_GETAUTOCOMMITSTREAMRESP']._serialized_end=2097
# @@protoc_insertion_point(module_scope)
