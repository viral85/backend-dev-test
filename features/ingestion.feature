Feature: Data ingestion
  Given that we have this extremely esoteric data source and
  time series database, we want to import messages from the source, into the
  time series database.

  Scenario: Everything alright
    Given that we get the correct data from esoteric source
    And that the esoteric time series database is available
    When when we run an import
    Then it's a success
