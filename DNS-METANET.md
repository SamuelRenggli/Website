# DNS switch for manuelstaehelin.ch

Goal: the website comes from GitHub Pages, **email stays exactly as it is** (Metanet server `urbanus`).

Status 8 Oct 2026: the domain uses the name servers `ns1/ns2.urbanus.metanet.ch`.
The active address book (DNS zone) is therefore in **Plesk** on the hosting, not in my.metanet.ch.

> **Done on 8 Oct 2026 with option B.** The domain now uses Metanet DNS (`ch.pro.io`, `nl.pro.io`,
> `p.dnh.net`). From now on, DNS changes are made **only in my.metanet.ch → DNS-Verwaltung**, not in Plesk.
> All 19 records below were checked against the previous zone (including DKIM).

There are two ways. **Option A is shorter and safer.**

---

## Option A (recommended): change 2 entries in Plesk

Whoever has the Plesk login (e.g. the friend) does this, about 5 minutes:

1. Log in at **https://urbanus.metanet.ch:8443**
2. **Websites & Domains** → **manuelstaehelin.ch** → **Hosting & DNS** → **DNS**
3. Find the line **`manuelstaehelin.ch.`  A  `80.74.140.2`** → click it → change the value to `185.199.108.153` → OK
4. Click **Add Record** three times, each time type **A**, domain name empty (= main domain), value:
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
5. Find the line **`www.manuelstaehelin.ch.`  A  `80.74.140.2`** → delete it
6. **Add Record**: type **CNAME**, domain name `www`, value `samuelrenggli.github.io.`
7. If a yellow banner says **"Update"** / **"Apply"** at the top: click it
8. Do **not** touch any other line.

Done. The name servers in my.metanet.ch stay unchanged.

---

## Option B: everything in my.metanet.ch (without Plesk)

Here the complete address book is rebuilt in Metanet's DNS management, then the domain is switched over.
**Every line in the table must be entered**, otherwise email stops working.

### Step 1: enter all records

In **my.metanet.ch** → domain **manuelstaehelin.ch** → tab **DNS-Verwaltung**.
Do **not** use "Vorlage anwenden". For each line: choose the type in the dropdown → **Hinzufügen** →
fill in name and value. "Name" empty means the main domain (in some forms: `@`).

**Website (new, GitHub Pages)**

| # | Type | Name | Value |
| --- | --- | --- | --- |
| 1 | A | *(empty)* | `185.199.108.153` |
| 2 | A | *(empty)* | `185.199.109.153` |
| 3 | A | *(empty)* | `185.199.110.153` |
| 4 | A | *(empty)* | `185.199.111.153` |
| 5 | CNAME | `www` | `samuelrenggli.github.io.` |

**Email (copy unchanged from the current zone)**

| # | Type | Name | Value |
| --- | --- | --- | --- |
| 6 | MX | *(empty)* | Priority `10`, server `mail.manuelstaehelin.ch.` |
| 7 | A | `mail` | `80.74.140.2` |
| 8 | A | `webmail` | `80.74.140.2` |
| 9 | A | `smtp` | `80.74.140.2` |
| 10 | A | `imap` | `80.74.140.2` |
| 11 | A | `pop` | `80.74.140.2` |
| 12 | A | `pop3` | `80.74.140.2` |
| 13 | A | `autodiscover` | `80.74.140.2` |
| 14 | A | `autoconfig` | `80.74.140.2` |
| 15 | A | `ftp` | `80.74.140.2` |
| 16 | TXT | *(empty)* | `v=spf1 include:_spf.sui-inter.net +mx +a ~all` |
| 17 | TXT | `_dmarc` | `v=DMARC1; p=quarantine; adkim=s; aspf=s` |
| 18 | TXT | `default._domainkey` | see below (DKIM, one long line) |
| 19 | SRV | `_imaps._tcp` | Priority `0`, weight `0`, port `993`, target `urbanus.metanet.ch.` |

Value for line 18 (copy completely, without line breaks):

```
v=DKIM1; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp0bJlXg/+c0meqf6HBPyQPcBL7aXV6hAEhZk/hO6UB1/tuDuI4qbWKF9j+76URWRO0vv02kqtRU7w2K5z6wpYZsySuJSOdTDmM6xeXx2s0QxUxFtoiiBDQl2rVIMmzSTUSw0T1BWtecZL1usiLsp470vg0a9nKxR9lMUdeY/8TpkiSyZJ/x1qr5DuPIMCKc0YGLgt05j+9jLYCn86n/q7HmW2AtCXugJ1KiC5SOacKentolQvFOZpiS7heY+heyDY3WlcZPcROW97H48B/C1N978p24bQ8uJNMDiLcwYCvx+aWNn7xmVA2aSyDNkgZqyP8YyuqHyROD/A5k/7kgACwIDAQAB;
```

Then **save the zone definition** (button at the bottom / top).

Leave the three existing **NS** lines (`ch.pro.io`, `nl.pro.io`, `p.dnh.net`) as they are.

### Step 2: check before switching

Tell Claude "DNS entered" before step 3. Claude can query Metanet's servers directly and compare
all 19 lines with the current zone, so nothing is missing.

### Step 3: switch the name servers

**Domain-Verwaltung** tab → name servers → change from `ns1/ns2.urbanus.metanet.ch` to the
Metanet DNS servers (`ch.pro.io`, `nl.pro.io`, `p.dnh.net`, or the "use Metanet DNS" option) → save.

It can take up to 48 hours until everyone sees the new servers. Email keeps working during that time,
because both address books point to the same mail server.

### Important for later (option B only)

After the switch, DNS changes are made **only in my.metanet.ch**, no longer in Plesk.
If the email server in Plesk ever gets a new DKIM key, the TXT `default._domainkey` must be
updated in my.metanet.ch by hand.

---

## After either option

1. Tell Claude, who checks that the new records are visible worldwide.
2. GitHub → repository **SamuelRenggli/Website** → **Settings** → **Pages** → **Custom domain**:
   `manuelstaehelin.ch` → **Save**. When the check is green: tick **Enforce HTTPS**.
3. Test https://manuelstaehelin.ch and https://www.manuelstaehelin.ch, and send yourself a test email.

## Switching back

- Option A: set the A record of the main domain back to `80.74.140.2`, delete the three extra A records,
  `www` back to A `80.74.140.2`.
- Option B: set the name servers back to `ns1.urbanus.metanet.ch` and `ns2.urbanus.metanet.ch`.
