# VAT Sense Python SDK

[![PyPI version](https://img.shields.io/pypi/v/vatsense.svg?label=pypi%20(stable))](https://pypi.org/project/vatsense/)

The official Python library for the [VAT Sense](https://vatsense.com) REST API. Validate VAT/EORI numbers, look up VAT/GST rates, calculate prices, convert currencies, and generate VAT-compliant invoices.

Includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Installation

```sh
pip install vatsense
```

Requires Python 3.9+.

## Quick start

Create a client using your API key from the [VAT Sense dashboard](https://vatsense.com/dashboard). The API uses HTTP Basic Auth with `user` as the username and your API key as the password.

```python
from vat_sense import VatSense

client = VatSense(
    username="user",
    password="your_api_key",
)
```

You can also set the `VAT_SENSE_USERNAME` and `VAT_SENSE_PASSWORD` environment variables and the client will pick them up automatically.

### Validate a VAT number

```python
response = client.validate.check(vat_number="GB288305674")

if response.data.valid:
    print(response.data.company.company_name)     # "BRITISH BROADCASTING CORPORATION"
    print(response.data.company.company_address)
    print(response.data.company.country_code)      # "GB"
```

VAT validation works for the UK, EU, Australia, Norway, Switzerland, South Africa, and Brazil.

### Validate an EORI number

```python
response = client.validate.check(eori_number="GB123456789000")

if response.data.valid:
    print(response.data.company.company_name)
```

EORI validation is available for UK and EU numbers only.

### Get a consultation number

If you need an official consultation number from VIES (EU) or HMRC (UK), provide your own VAT number as the requester:

```python
response = client.validate.check(
    vat_number="FR12345678901",
    requester_vat_number="FR98765432101",
)

print(response.data.consultation_number)
```

> **Note:** GB requester numbers only work for GB validations, and EU requester numbers only work for EU validations. Cross-region requests are not supported.

### Find the VAT rate for a country

```python
rate = client.rates.find(country_code="DE")

print(rate.data.country_name)       # "Germany"
print(rate.data.tax_rate.rate)      # 19.0
print(rate.data.tax_rate.class_)    # "standard"
```

### Find a rate for a specific product type

```python
rate = client.rates.find(country_code="DE", type="ebooks")

print(rate.data.tax_rate.rate)      # 7.0
print(rate.data.tax_rate.class_)    # "reduced"
```

### Find a rate by IP address

Useful for determining the correct rate based on your customer's location:

```python
rate = client.rates.find(ip_address="185.86.151.11")

print(rate.data.country_code)       # "GB"
print(rate.data.tax_rate.rate)      # 20.0
```

### Calculate a VAT-inclusive price

```python
result = client.rates.calculate_price(
    price="100.00",
    tax_type="excl",
    country_code="FR",
)

print(result.data.vat_price.price_incl_vat)  # Price including VAT
print(result.data.vat_price.price_excl_vat)  # Price excluding VAT
print(result.data.vat_price.vat_rate)        # VAT rate applied
print(result.data.vat_price.vat)             # VAT amount
```

### List all VAT rates

```python
rates = client.rates.list()

for rate in rates.data:
    print(f"{rate.country_code}: {rate.country_name}")

# Filter to EU countries only
eu_rates = client.rates.list(eu=True)
```

### Async usage

An async client is also available:

```python
import asyncio
from vat_sense import AsyncVatSense

client = AsyncVatSense(
    username="user",
    password="your_api_key",
)

async def main():
    response = await client.validate.check(vat_number="GB288305674")
    print(response.data.valid)

asyncio.run(main())
```

## Handling errors

When the API returns an error, the library raises a typed exception:

```python
from vat_sense import VatSense, APIConnectionError, APIStatusError, RateLimitError

client = VatSense(username="user", password="your_api_key")

try:
    response = client.validate.check(vat_number="GB288305674")
except APIConnectionError:
    # Network issue, could not reach the API
    print("Connection failed")
except RateLimitError:
    # 429: Too many requests (300/min general limit, 3/sec for UK validation)
    print("Rate limited, try again shortly")
except APIStatusError as e:
    # Covers all other HTTP errors
    print(e.status_code)
    print(e.message)
```

A `412` error means the upstream validation service (VIES, HMRC, etc.) is temporarily unavailable. These requests do not count against your usage quota.

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 404         | `NotFoundError`            |
| 409         | `ConflictError`            |
| 429         | `RateLimitError`           |
| >= 500      | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

## Retries

Failed requests are automatically retried up to 2 times with exponential backoff. This includes connection errors, timeouts, 429, and 5xx responses.

```python
# Disable retries
client = VatSense(username="user", password="your_api_key", max_retries=0)

# Or configure per request
response = client.validate.check(vat_number="GB288305674", timeout=5.0)
```

## Available services

| Service              | Description                                     |
| -------------------- | ----------------------------------------------- |
| `client.validate`    | Validate VAT and EORI numbers                   |
| `client.rates`       | VAT/GST rate lookups, price calculations         |
| `client.countries`   | Country data and province lookups                |
| `client.currency`    | Exchange rates and currency conversion           |
| `client.invoice`     | Create and manage VAT-compliant invoices         |
| `client.usage`       | Check your API usage                             |

## Documentation

Full API documentation is available at [vatsense.com/documentation](https://vatsense.com/documentation).

## Versioning

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions. As the library is in initial development and has a major version of `0`, APIs may change at any time.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
