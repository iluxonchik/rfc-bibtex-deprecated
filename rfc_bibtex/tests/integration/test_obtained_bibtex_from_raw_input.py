"""
Integration tests related to reading raw list of RFCs providied in a text file (one per line)
and directly as command-line args.
"""
import vcr
from .base import BaseRFCBibTexIntegrationTestCase
from rfc_bibtex.rfc_bibtex import RFCBibtex

"""
Integration tests written to support the addition of the feature that allows
to parse RFC names from .tex and .aux files.

NOTE: the tests are written with the migrations that will be done in consideration.
      For example, the URLs from which the RFC will be obtained will be changed,
      with this, there is also a change in the returned content. For this reason,
      tests were adapted to work in both of them. This is why some assertions might
      seem like incomplete. Later, the tests should and will be refactored.
"""
class TestObtainedBibtexFromRawRFCInput(BaseRFCBibTexIntegrationTestCase):
    TLS_RFCS_FILE_PATH = BaseRFCBibTexIntegrationTestCase.TEST_RESOURCES_PATH + "tls_rfcs.txt"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @vcr.use_cassette(path='rfc_bibtex/tests/integration/resources/fixtures/vcr_cassettes/synopsis.yaml')
    def test_reading_rfcs_from_command_line_returns_expected_latex(self):
        rfc_bibtex = RFCBibtex(['RFC5246', 'draft-ietf-tls-tls13-21', 'RFC8446'])
        entries = list(rfc_bibtex.bibtex_entries)
        self.assertIn("RFC5246", entries[0])
        self.assertIn("The Transport Layer Security (TLS) Protocol Version 1.2", entries[0])
        self.assertIn("2008", entries[0])
        self.assertIn("RFC Editor", entries[0])

        self.assertIn("{draft-ietf-tls-tls13-21}", entries[1])
        self.assertIn("The Transport Layer Security (TLS) Protocol Version 1.3", entries[1])

        self.assertIn("RFC8446", entries[2])
        self.assertIn("The Transport Layer Security (TLS) Protocol Version 1.3", entries[1])
        self.assertIn("2018", entries[2])
        self.assertIn("RFC Editor", entries[2])

    @vcr.use_cassette(path='rfc_bibtex/tests/integration/resources/fixtures/vcr_cassettes/synopsis.yaml')
    def test_reading_rfcs_from_file_returns_expected_latex(self):
        rfc_bibtex = RFCBibtex(in_file_name=self.TLS_RFCS_FILE_PATH)
        entries = list(rfc_bibtex.bibtex_entries)
        self.assertIn("RFC5246", entries[0])
        self.assertIn("The Transport Layer Security (TLS) Protocol Version 1.2", entries[0])
        self.assertIn("2008", entries[0])
        self.assertIn("RFC Editor", entries[0])

        self.assertIn("{draft-ietf-tls-tls13-21}", entries[1])
        self.assertIn("The Transport Layer Security (TLS) Protocol Version 1.3", entries[1])

        self.assertIn("RFC8446", entries[2])
        self.assertIn("The Transport Layer Security (TLS) Protocol Version 1.3", entries[1])
        self.assertIn("2018", entries[2])
        self.assertIn("RFC Editor", entries[2])

