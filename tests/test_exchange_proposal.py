"""Validate exchange proposals against the published Draft 7 schema."""

import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft7Validator


class ExchangeProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema_path = (
            Path(__file__).resolve().parents[1]
            / "messages/stage-1/exchange-proposal-message.json"
        )
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft7Validator.check_schema(schema)
        cls.validator = Draft7Validator(schema)

    def setUp(self):
        # Synthetic identifiers and signatures; these tests validate structure only.
        claim = {
            "digitalAssetId": "asset-1",
            "assetProfileId": "profile-1",
            "verifiedOriginatorEntityId": "originator-1",
            "verifiedBeneficiaryEntityId": "beneficiary-1",
            "originatorPubkey": "originator-key",
            "beneficiaryPubkey": "beneficiary-key",
            "senderGatewaySignaturePublicKey": "sender-key",
            "receiverGatewaySignaturePublicKey": "receiver-key",
            "senderGatewayNetworkId": "network-1",
            "recipientGatewayNetworkId": "network-2",
        }
        self.claims = [dict(claim, digitalAssetId=f"asset-{i}") for i in range(1, 4)]
        self.proposal = {
            "version": "1.0",
            "messageType": "exchange-proposal-msg",
            "sessionId": "session-1",
            "exchangeContextId": "exchange-1",
            "exchangeInitClaims": copy.deepcopy(self.claims[:2]),
            "exchangeInitClaimsFormat": "json",
            "networkCapabilitiesList": "test-capabilities",
            "clientSignature": "test-signature",
        }

    def test_requires_exactly_two_claims(self):
        for count in (0, 1, 2, 3):
            with self.subTest(claim_count=count):
                proposal = dict(self.proposal, exchangeInitClaims=self.claims[:count])
                self.assertEqual(self.validator.is_valid(proposal), count == 2)

    def test_rejects_missing_asset_id(self):
        del self.proposal["exchangeInitClaims"][0]["digitalAssetId"]
        self.assertFalse(self.validator.is_valid(self.proposal))

    def test_rejects_non_array_claims(self):
        self.proposal["exchangeInitClaims"] = "not-an-array"
        self.assertFalse(self.validator.is_valid(self.proposal))

    def test_rejects_non_string_asset_id(self):
        self.proposal["exchangeInitClaims"][0]["digitalAssetId"] = 123
        self.assertFalse(self.validator.is_valid(self.proposal))


if __name__ == "__main__":
    unittest.main()
