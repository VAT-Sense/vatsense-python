# Rates

Types:

```python
from vat_sense.types import (
    FindRate,
    Rate,
    TaxRate,
    RateListResponse,
    RateCalculatePriceResponse,
    RateListTypesResponse,
)
```

Methods:

- <code title="get /rates">client.rates.<a href="./src/vat_sense/resources/rates.py">list</a>(\*\*<a href="src/vat_sense/types/rate_list_params.py">params</a>) -> <a href="./src/vat_sense/types/rate_list_response.py">RateListResponse</a></code>
- <code title="get /rates/price">client.rates.<a href="./src/vat_sense/resources/rates.py">calculate_price</a>(\*\*<a href="src/vat_sense/types/rate_calculate_price_params.py">params</a>) -> <a href="./src/vat_sense/types/rate_calculate_price_response.py">RateCalculatePriceResponse</a></code>
- <code title="get /rates/tax_rate">client.rates.<a href="./src/vat_sense/resources/rates.py">details</a>(\*\*<a href="src/vat_sense/types/rate_details_params.py">params</a>) -> <a href="./src/vat_sense/types/find_rate.py">FindRate</a></code>
- <code title="get /rates/rate">client.rates.<a href="./src/vat_sense/resources/rates.py">find</a>(\*\*<a href="src/vat_sense/types/rate_find_params.py">params</a>) -> <a href="./src/vat_sense/types/find_rate.py">FindRate</a></code>
- <code title="get /rates/types">client.rates.<a href="./src/vat_sense/resources/rates.py">list_types</a>() -> <a href="./src/vat_sense/types/rate_list_types_response.py">RateListTypesResponse</a></code>

# Countries

Types:

```python
from vat_sense.types import Country, CountryListResponse, CountryListProvincesResponse
```

Methods:

- <code title="get /countries">client.countries.<a href="./src/vat_sense/resources/countries.py">list</a>(\*\*<a href="src/vat_sense/types/country_list_params.py">params</a>) -> <a href="./src/vat_sense/types/country_list_response.py">CountryListResponse</a></code>
- <code title="get /countries/provinces">client.countries.<a href="./src/vat_sense/resources/countries.py">list_provinces</a>(\*\*<a href="src/vat_sense/types/country_list_provinces_params.py">params</a>) -> <a href="./src/vat_sense/types/country_list_provinces_response.py">CountryListProvincesResponse</a></code>

# Validate

Types:

```python
from vat_sense.types import ValidateCheckResponse
```

Methods:

- <code title="get /validate">client.validate.<a href="./src/vat_sense/resources/validate.py">check</a>(\*\*<a href="src/vat_sense/types/validate_check_params.py">params</a>) -> <a href="./src/vat_sense/types/validate_check_response.py">ValidateCheckResponse</a></code>

# Currency

Types:

```python
from vat_sense.types import (
    VatPrice,
    CurrencyListResponse,
    CurrencyCalculateVatPriceResponse,
    CurrencyConvertResponse,
)
```

Methods:

- <code title="get /currency">client.currency.<a href="./src/vat_sense/resources/currency.py">list</a>(\*\*<a href="src/vat_sense/types/currency_list_params.py">params</a>) -> <a href="./src/vat_sense/types/currency_list_response.py">CurrencyListResponse</a></code>
- <code title="get /currency/price">client.currency.<a href="./src/vat_sense/resources/currency.py">calculate_vat_price</a>(\*\*<a href="src/vat_sense/types/currency_calculate_vat_price_params.py">params</a>) -> <a href="./src/vat_sense/types/currency_calculate_vat_price_response.py">CurrencyCalculateVatPriceResponse</a></code>
- <code title="get /currency/convert">client.currency.<a href="./src/vat_sense/resources/currency.py">convert</a>(\*\*<a href="src/vat_sense/types/currency_convert_params.py">params</a>) -> <a href="./src/vat_sense/types/currency_convert_response.py">CurrencyConvertResponse</a></code>

# Invoice

Types:

```python
from vat_sense.types import (
    CreateInvoice,
    Invoice,
    InvoiceConversionInput,
    InvoiceResponse,
    InvoiceListResponse,
    InvoiceDeleteResponse,
)
```

Methods:

- <code title="post /invoice">client.invoice.<a href="./src/vat_sense/resources/invoice/invoice.py">create</a>(\*\*<a href="src/vat_sense/types/invoice_create_params.py">params</a>) -> <a href="./src/vat_sense/types/invoice_response.py">InvoiceResponse</a></code>
- <code title="get /invoice/{invoice_id}">client.invoice.<a href="./src/vat_sense/resources/invoice/invoice.py">retrieve</a>(invoice_id) -> <a href="./src/vat_sense/types/invoice_response.py">InvoiceResponse</a></code>
- <code title="patch /invoice/{invoice_id}">client.invoice.<a href="./src/vat_sense/resources/invoice/invoice.py">update</a>(invoice_id, \*\*<a href="src/vat_sense/types/invoice_update_params.py">params</a>) -> <a href="./src/vat_sense/types/invoice_response.py">InvoiceResponse</a></code>
- <code title="get /invoice">client.invoice.<a href="./src/vat_sense/resources/invoice/invoice.py">list</a>(\*\*<a href="src/vat_sense/types/invoice_list_params.py">params</a>) -> <a href="./src/vat_sense/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="delete /invoice/{invoice_id}">client.invoice.<a href="./src/vat_sense/resources/invoice/invoice.py">delete</a>(invoice_id) -> <a href="./src/vat_sense/types/invoice_delete_response.py">InvoiceDeleteResponse</a></code>

## Item

Types:

```python
from vat_sense.types.invoice import InvoiceItem, InvoiceItemInput, ItemRetrieveResponse
```

Methods:

- <code title="get /invoice/{invoice_id}/item/{item_id}">client.invoice.item.<a href="./src/vat_sense/resources/invoice/item.py">retrieve</a>(item_id, \*, invoice_id) -> <a href="./src/vat_sense/types/invoice/item_retrieve_response.py">ItemRetrieveResponse</a></code>
- <code title="patch /invoice/{invoice_id}/item/{item_id}">client.invoice.item.<a href="./src/vat_sense/resources/invoice/item.py">update</a>(item_id, \*, invoice_id, \*\*<a href="src/vat_sense/types/invoice/item_update_params.py">params</a>) -> <a href="./src/vat_sense/types/invoice_response.py">InvoiceResponse</a></code>
- <code title="delete /invoice/{invoice_id}/item/{item_id}">client.invoice.item.<a href="./src/vat_sense/resources/invoice/item.py">delete</a>(item_id, \*, invoice_id) -> <a href="./src/vat_sense/types/invoice_response.py">InvoiceResponse</a></code>
- <code title="post /invoice/{invoice_id}/item">client.invoice.item.<a href="./src/vat_sense/resources/invoice/item.py">add</a>(invoice_id, \*\*<a href="src/vat_sense/types/invoice/item_add_params.py">params</a>) -> <a href="./src/vat_sense/types/invoice_response.py">InvoiceResponse</a></code>

# Usage

Types:

```python
from vat_sense.types import UsageRetrieveResponse
```

Methods:

- <code title="get /usage">client.usage.<a href="./src/vat_sense/resources/usage.py">retrieve</a>() -> <a href="./src/vat_sense/types/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

# Sandbox

Types:

```python
from vat_sense.types import SandboxGenerateKeyResponse
```

Methods:

- <code title="post /sandbox/key">client.sandbox.<a href="./src/vat_sense/resources/sandbox.py">generate_key</a>() -> <a href="./src/vat_sense/types/sandbox_generate_key_response.py">SandboxGenerateKeyResponse</a></code>
