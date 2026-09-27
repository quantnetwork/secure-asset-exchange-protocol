# Secure Asset Exchange Protocol
This repository contains information relating to a proposed asset exchange modification of IETF's 'Secure Asset Transfer Protocol' standard. We call this proposed protocol, the 'Secure Asset Exchange Protocol' (SAEP). 

The SAEP enables assets on different ledgers to be swapped between users, without transferring those assets off their respective ledgers.

A potential use case of SAEP is to swap central bank digital currencies (CBDCs) that reside on different ledgers.

## Secure Asset Exchange Protocol Message Definitions

The messages and parameters of SAEP are based on the messages and parameters defined in [SATP](https://datatracker.ietf.org/doc/draft-ietf-satp-core/).

## IETF Link

This SAEP proposal to IETF is in the draft stage and can currently be found here: [https://github.com/ietf-satp/draft-marstein-satp-asset-exchange](https://github.com/ietf-satp/draft-marstein-satp-asset-exchange).

## Schema tests

Run the exchange proposal validation tests from the repository root:

```sh
python -m pip install jsonschema==4.26.0
python -B -m unittest discover -s tests -v
```

The tests use synthetic messages to check JSON Schema validation only.
