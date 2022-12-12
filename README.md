# gopass-MaskedEmail Proof of Concept

This is a quick PoC to demo an integration between the **gopass** password manager and the **Masked Email** feature (e.g., as used by Fastmail).

via [Fastmail](https://www.fastmail.help/hc/en-us/articles/4406536368911-Masked-Email):
> A Masked Email address is a unique, automatically generated email address that can be used in place of your real email address.
>
> Masked Email addresses are especially useful when you need to sign up with new services online. Instead of sharing your real email address, keep it private and protect yourself from data breaches and spam by creating a new Masked Email for every service.


## Concept

When creating a new account on a website, the registration form usually requires at least `email address` and `password`. Obviously we want to manage the latter with *gopass*. 
Since *MaskedEmail* allows us to create an individual (masked) email address for each account we create, we want to include the creation of this email address into the process that also generates and stores the password. 
Thankfully, management of masked email addresses is available via JMAP.

1) Initialize process with
  - the name of the website as parameter (i.e., name of the password in gopass)
  - some additional data/comment (for the metadata of the mail address, and/or the gopass storage)
2) Call to MaskedEmail JMAP endpoint 
  - `state`: *enabled*
  - `forDomain`: the domain from step 1, e.g., *example.com*
  - `description`: the optional description from step 1
  - `url`: the gopass identifier from step 1, e.g., *gopass websites/example.com*
  - `emailPrefix`: TODO
  - returns `email`: the new email address and its `id`
3) Execute `gopass generate --clip` with
  - secret name: the gopass identifier from step 1, plus the email address from step 2
  - as a result, the newly generated password is stored and copied into the clipboard 


### Progress

- [X] find JMAP library that supports MaskedEmail
- [X] Experiment: Get existing MaskedEmail addresses via API → `experiment_get.py`
- [ ] Experiment: Manually create MaskedEmail via API
- [ ] Create MaskedEmail via API
- [ ] Create gopass secret with generated email address
- [ ] Other gopass options (e.g., password generator/lang, and password length)
- [ ] Storage of optional fields (e.g., description) after step 3 
- [ ] Create gopass issue to discuss this 
- *Other ideas:*
  - [ ] after step 2, copy generated email address into clipboard, and wait until user hits a key before proceeding (to give user time to paste the email address into the registration form)
  - [ ] Alsop put JMAP authentication token into gopass
  - [ ] Also add TOTP secret (usually not done during registration, though)
  - [ ] Support for API endpoints other than Fastmail 



## Resources

- [gopass](https://github.com/gopasspw/gopass)
- JMAP:
  - [Website](https://jmap.io) 
  - [Wikipedia: JMAP](https://en.wikipedia.org/wiki/JSON_Meta_Application_Protocol)
- [jmapc: A JMAP client library for Python](https://github.com/smkent/jmapc)
  - [Issue about MaskedEmail support](https://github.com/smkent/jmapc/issues/66)
- [maskedemail-cli](https://github.com/dvcrn/maskedemail-cli) in go
- Fastmail:
  - [Masked Email Documentation](https://www.fastmail.help/hc/en-us/articles/4406536368911-Masked-Email) 
  - [Masked Email API](https://www.fastmail.com/developer/maskedemail/) 
