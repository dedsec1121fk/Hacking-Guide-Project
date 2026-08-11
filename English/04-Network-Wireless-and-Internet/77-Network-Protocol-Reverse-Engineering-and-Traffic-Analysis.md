# Network Protocol Reverse Engineering and Traffic Analysis

> **Purpose:** Learn how to reconstruct an unknown or poorly documented protocol from packet captures and a controlled implementation you own.

## Learning objectives

- Separate transport framing from application semantics.
- Infer fields, lengths, message types, state, checksums, and encodings.
- Use controlled input variation to identify field meaning.
- Distinguish encrypted, compressed, encoded, and binary data.
- Build a minimal protocol specification from evidence.

## Start below the application

Before interpreting payload bytes, identify transport facts: TCP, UDP, QUIC, Unix socket, serial, BLE characteristic, or another carrier. TCP is a byte stream, not a message protocol. Application message boundaries must be defined separately by lengths, delimiters, fixed-size records, higher-level framing, or connection lifecycle.

UDP preserves datagram boundaries but applications may still fragment logical messages themselves.

## Direction and roles

Determine which endpoint initiates the connection and which sends the first application message. Label directions `client → server` and `server → client` rather than relying on IP addresses that may change.

Identify handshake, steady-state requests, responses, keepalives, errors, and shutdown behavior.

## Capture discipline

For a protocol you own, capture one simple action at a time:

1. connect and do nothing;
2. connect and authenticate using synthetic credentials if the lab requires it;
3. perform action A once;
4. repeat A with one field changed;
5. perform action B;
6. intentionally cause a benign validation error;
7. disconnect cleanly.

The controlled variation makes field inference much stronger.

## Hex and ASCII views

Binary analysis uses both byte offsets and decoded representations. ASCII/UTF-8 text may be embedded among binary lengths and identifiers. Repeated constants can indicate magic values, protocol versions, opcodes, separators, or flags.

Do not assume a recognizable string means the entire protocol is text-based.

## Fixed header hypothesis

Many protocols start with a fixed header containing fields such as:

- magic/version;
- message type;
- flags;
- sequence/request ID;
- payload length;
- checksum;
- timestamp.

Compare multiple messages and mark bytes that remain constant, increment, correlate with payload size, or change with action type.

## Endianness

To infer integer byte order, choose a value you can control. If setting a synthetic count to `0x0102` yields bytes `01 02`, the field is big-endian; `02 01` suggests little-endian. Confirm with more than one value.

Network standards often use big-endian, but custom protocols may not.

## Length-prefixed framing

If a field changes exactly with message size, test whether it includes the header itself or only payload. A common parser bug occurs when sender and receiver disagree about units, signedness, maximum size, or nested lengths.

Your protocol specification should state exact offset, width, endian, allowed range, and whether the field includes headers.

## Type-length-value structures

TLV designs encode a type identifier, a length, then a value. Variants may align/pad fields, nest TLVs, or use variable-length integers. Once you suspect TLV, compare messages with optional fields and see whether unknown elements can be skipped based on their declared length.

## Checksums and integrity

A changing field near the end/header may be a checksum, MAC, or hash. A checksum detects accidental corruption but does not prove authenticity. A keyed MAC provides authenticity/integrity when keys are protected.

Do not attempt to defeat authentication in third-party protocols. In your own lab, simply identify whether a field changes with payload and consult source/specification afterward.

## Compression versus encryption

High-entropy payloads can result from encryption, compression, or encoded binary data. Clues include handshake negotiation, fixed magic headers, length behavior, repeated plaintext metadata, and whether identical inputs produce identical output.

Encryption should be assumed opaque unless you possess legitimate keys in your own environment.

## Stateful protocols

A message may only be valid after a handshake or prior state transition. Build a state diagram. Track sequence numbers, session IDs, negotiated version/features, authentication state, and timeouts.

Protocol security often fails when a parser accepts a message in the wrong state.

## Error messages as an oracle

In your own implementation, errors reveal parser expectations. Compare malformed-but-benign local inputs: truncated message, unsupported version, unknown type, invalid length. Map each failure to the validation stage.

A production protocol should avoid leaking unnecessary secrets while still logging enough server-side detail for diagnosis.

## Wireshark/tshark methodology

If using packet-analysis tools, begin with filters that isolate your own lab endpoints and one connection. Follow the stream, mark message boundaries, export only the payloads you are authorized to analyze, and annotate offsets.

A custom Wireshark dissector is an excellent advanced project after you understand the format. It turns reverse-engineered fields into reusable analysis and can improve defensive visibility.

## Python parser project

Once the format is understood, write a parser that:

- accepts bytes, not a network target;
- validates minimum header length;
- checks declared lengths before slicing;
- rejects unsupported versions/types;
- uses explicit endian conversions;
- returns structured fields;
- preserves unknown fields safely;
- never allocates unbounded memory from a declared length.

Then fuzz the parser locally using Module 68.

## Safe lab

Write a tiny localhost client/server with a custom frame: 4-byte magic, 1-byte version, 1-byte type, 2-byte big-endian payload length, payload. Capture three benign message types and reverse the format without looking at the server source. Then compare with source.

## Guided study workflow

### Before you begin

Complete Modules 08, 20, 51, 61, 68, and 78 when available.

### Practice task

Reverse-engineer a protocol you wrote yourself from a packet capture, then implement a standalone parser and a short specification.

### Evidence to keep

PCAP from the private lab, annotated hex, state diagram, inferred field table, parser, and source comparison.

### Common mistakes to avoid

- treating TCP packets as application messages;
- guessing endian from one sample;
- mistaking compression for encryption;
- capturing third-party/private traffic;
- writing a parser that trusts declared lengths.

### Mastery check

Given several captures, explain how you would infer framing, field width, endian, and state without access to source code.

### Continue with

Modules **78, 79, 80, 83, and 85**.
