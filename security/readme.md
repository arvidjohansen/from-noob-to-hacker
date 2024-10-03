### Cheat Sheet: Basics of Cryptography Key Generation and Using SOPS

#### 1. Key Generation Basics

- **SSH Keys**:

  - Commonly used for secure access to servers.
  - Generated using tools like `ssh-keygen`.
  - Consist of a private key (kept secret) and a public key (shared).
- **PGP Keys**:

  - Used for encrypting and signing data.
  - Generated using tools like `gpg` (GNU Privacy Guard).
  - Also consist of a private key and a public key.

#### 2. Understanding SOPS (Secret OPerationS)

- **SOPS**:
  - A tool for managing secrets that can be encrypted/decrypted using various keys.
  - Supports AWS KMS, GCP KMS, Azure Key Vault, age, and PGP keys.

#### 3. Why Convert SSH Key to PGP Format?

- **Different Formats**:

  - SSH and PGP keys are designed for different purposes and have different formats.
  - SSH keys are optimized for secure login and authentication.
  - PGP keys are optimized for encryption and digital signing.
- **Need for Conversion**:

  - SOPS can use PGP keys for encryption.
  - Converting an SSH key to PGP allows you to use your existing SSH key infrastructure with SOPS.

#### 4. How to Convert SSH Key to PGP Key

- **Using `gpg`**:
  1. **Export SSH Public Key**:
     ```sh
     ssh-keygen -e -f ~/.ssh/id_rsa.pub -m PKCS8 > id_rsa_pub.pem
     ```
  2. **Import SSH Public Key into GPG**:
     ```sh
     gpg --import < id_rsa_pub.pem
     ```

#### 5. Why Are There Different Key Formats?

- **Purpose-Specific Design**:

  - **SSH Keys**: Designed for authentication in SSH sessions.
  - **PGP Keys**: Designed for encrypting data and verifying signatures.
- **Compatibility**:

  - Different software and protocols may require different key formats.
  - Converting keys allows you to use the same underlying key material across various systems.

#### 6. Best Practices

- **Key Management**:

  - Keep private keys secure and never share them.
  - Use strong passphrases for private keys.
  - Regularly rotate keys to minimize risk if they are compromised.
- **Using SOPS**:

  - Use PGP keys for encryption within SOPS for better compatibility and security.
  - Store keys securely (e.g., using a key management service or hardware security module).
- **Converting Keys**:

  - Ensure that the conversion process maintains the integrity and security of the keys.
  - Verify the imported keys after conversion.

#### 7. Common Commands

- **Generate SSH Key**:

  ```sh
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```
- **Generate PGP Key**:

  ```sh
  gpg --full-generate-key
  ```
- **List GPG Keys**:

  ```sh
  gpg --list-keys
  ```
- **Encrypt with GPG**:

  ```sh
  gpg --encrypt --recipient "recipient@example.com" file.txt
  ```
- **Decrypt with GPG**:

  ```sh
  gpg --decrypt file.txt.gpg
  ```
- **Encrypt File with SOPS**:

  ```sh
  sops --encrypt --pgp <KEY_ID> file.txt > file.enc.txt
  ```
- **Decrypt File with SOPS**:

  ```sh
  sops --decrypt file.enc.txt > file.txt
  ```


| Use Case                                            | Command/Action                                                                                           | Example: Bob Sends Message to Alice            | Textual Representation Before Encryption                | Encrypted Representation              | Decryption Command                                                   | Decrypted Representation                                |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------- |
| **Decrypt JSON File**                               | `sops -d secrets.enc.json`                                                                               | Alice decrypts JSON file                       | -                                                       | SOPS encrypted JSON structure         | `sops -d secrets.enc.json`                                           | `{"message": "Hi Alice, it's Bob"}`                     |
| **Encrypt Environment Variables**                   | `sops -e .env > .env.enc`                                                                                | Bob encrypts environment variables             | `MESSAGE="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `sops -d .env.enc`                                                   | `MESSAGE="Hi Alice, it's Bob"`                          |
| **Decrypt Environment Variables**                   | `sops -d .env.enc > .env`                                                                                | Alice decrypts environment variables           | -                                                       | SOPS encrypted YAML/JSON structure    | `sops -d .env.enc`                                                   | `MESSAGE="Hi Alice, it's Bob"`                          |
| **View File Metadata**                              | `sops -m secrets.txt`                                                                                    | Bob views metadata of encrypted file           | -                                                       | SOPS metadata output                  | -                                                                    | -                                                       |
| **Rotate Data Key**                                 | `sops -r -i secrets.txt`                                                                                 | Bob rotates encryption key                     | -                                                       | SOPS encrypted YAML/JSON structure    | -                                                                    | -                                                       |
| **Set Output Format**                               | `sops -o json -e secrets.txt > secrets.enc.json`                                                         | Bob sets output format to JSON                 | `message="Hi Alice, it's Bob"`                          | SOPS encrypted JSON structure         | `sops -d secrets.enc.json`                                           | `{"message": "Hi Alice, it's Bob"}`                     |
| **Decrypt to Specific File**                        | `sops -d secrets.txt -o output.txt`                                                                      | Alice saves decrypted message to specific file | -                                                       | SOPS encrypted YAML/JSON structure    | `sops -d secrets.txt -o output.txt`                                  | `message="Hi Alice, it's Bob"`                          |
| **Use SOPS with Terraform**                         | `terraform init && terraform plan -var-file=secrets.enc`                                                 | Bob integrates secrets with Terraform          | `variable "message" { default = "Hi Alice, it's Bob" }` | SOPS encrypted file used in Terraform | -                                                                    | `variable "message" { default = "Hi Alice, it's Bob" }` |
| **Use SOPS with Ansible**                           | `ansible-vault encrypt secrets.txt --vault-password-file ~/.sops/.sops_vault`                            | Bob integrates secrets with Ansible            | `message="Hi Alice, it's Bob"`                          | Encrypted using Ansible Vault         | -                                                                    | `message="Hi Alice, it's Bob"`                          |
| **Encrypt File with Custom GPG Key**                | `sops --pgp "John Doe <john.doe@example.com>" -e secrets.txt > secrets.enc`                              | Bob encrypts using custom GPG key              | `message="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `sops -d secrets.enc`                                                | `message="Hi Alice, it's Bob"`                          |
| **Decrypt Using a Specific Key**                    | `sops --pgp <PGP_KEY_FINGERPRINT> -d secrets.enc`                                                        | Alice decrypts with specific GPG key           | -                                                       | SOPS encrypted YAML/JSON structure    | `sops --pgp <PGP_KEY_FINGERPRINT> -d secrets.enc`                    | `message="Hi Alice, it's Bob"`                          |
| **Encrypt File Using Key from AWS Secrets Manager** | `sops --aws-secret arn:aws:secretsmanager:region:acct-id:secret:key-id -e secrets.txt > secrets.enc`     | Bob uses AWS Secrets Manager key               | `message="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `sops -d secrets.enc`                                                | `message="Hi Alice, it's Bob"`                          |
| **Use SOPS with Docker**                            | `docker run -v $(pwd):/secrets mozilla/sops -e /secrets/secrets.txt > /secrets/secrets.enc`              | Bob uses SOPS in Docker container              | `message="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `docker run -v $(pwd):/secrets mozilla/sops -d /secrets/secrets.enc` | `message="Hi Alice, it's Bob"`                          |
| **Encrypt File with Age**                           | `sops --age age1... -e secrets.txt > secrets.enc`                                                        | Bob uses Age to encrypt message                | `message="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `sops --age age1... -d secrets.enc`                                  | `message="Hi Alice, it's Bob"`                          |
| **Decrypt File with Age**                           | `sops --age age1... -d secrets.enc`                                                                      | Alice decrypts with Age                        | -                                                       | SOPS encrypted YAML/JSON structure    | `sops --age age1... -d secrets.enc`                                  | `message="Hi Alice, it's Bob"`                          |
| **Generate Age Key**                                | `age-keygen -o key.txt`                                                                                  | Bob generates Age key                          | -                                                       | -                                     | -                                                                    | -                                                       |
| **Rotate Key with GCP KMS**                         | `sops -r --gcp-kms projects/project-id/locations/global/keyRings/key-ring/cryptoKeys/key -i secrets.txt` | Bob rotates key with GCP KMS                   | -                                                       | SOPS encrypted YAML/JSON structure    | -                                                                    | -                                                       |
| **Rotate Key with AWS KMS**                         | `sops -r --kms arn:aws:kms:region:acct-id:key/key-id -i secrets.txt`                                     | Bob rotates key with AWS KMS                   | -                                                       | SOPS encrypted YAML/JSON structure    | -                                                                    | -                                                       |
| **View Decrypted JSON Inline**                      | `cat secrets.enc.json                                                                                    | sops -d /dev/stdin`                            | Alice views decrypted JSON inline                       | -                                     | SOPS encrypted JSON structure                                        | `cat secrets.enc.json                                   |
| **Edit File with Vim**                              | `EDITOR=vim sops secrets.txt`                                                                            | Bob edits file with Vim                        | `message="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `EDITOR=vim sops secrets.txt`                                        | `message="Hi Alice, it's Bob"`                          |
| **Automate Encryption in CI/CD**                    | `sops -e secrets.txt > secrets.enc`                                                                      | Bob automates encryption in CI/CD              | `message="Hi Alice, it's Bob"`                          | SOPS encrypted YAML/JSON structure    | `sops -d secrets.enc > secrets.txt`                                  | `message="Hi Alice, it's Bob"`                          |
| **Decrypt in CI/CD Pipeline**                       | `sops -d secrets.enc > secrets.txt`                                                                      | Alice automates decryption in CI/CD            | -                                                       | SOPS encrypted YAML/JSON structure    | `sops -d secrets.enc > secrets.txt`                                  | `message="Hi Alice, it's Bob"`                          |


Absolutely, let's add rows to explain these principles in detail:


| **Feature**                 | **SSH Encryption**                                                                                                | **PGP Encryption**                                                                                               | **Similarity**                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                 | Secure remote login and command execution                                                                         | Secure email communication and file encryption                                                                   | Both aim to provide security in data transmission and storage.                                                                      |
| **Encryption Algorithms**   | Typically uses RSA, DSA, ECDSA, and Ed25519                                                                       | Uses RSA, DSA, and ElGamal                                                                                       | Both use public-key cryptography for encryption.                                                                                    |
| **Symmetric Encryption**    | Uses symmetric encryption like AES for the session                                                                | Uses symmetric encryption like AES, CAST5, Triple DES                                                            | Both use symmetric encryption for encrypting the bulk of the data after establishing a secure channel.                              |
| **Key Management**          | SSH keys are managed manually, often through key files                                                            | PGP keys are managed via a keyring and may use a web of trust                                                    | Both require secure management of private and public keys.                                                                          |
| **Authentication**          | Public key, password, or host-based                                                                               | Public key and digital signatures                                                                                | Both provide methods for authenticating the identity of the communicating parties.                                                  |
| **Data Integrity**          | Ensures data integrity through HMAC (Hash-based Message Authentication Code)                                      | Ensures data integrity through cryptographic signatures                                                          | Both use mechanisms to ensure that the data has not been altered during transmission.                                               |
| **Non-repudiation**         | Not inherently provided                                                                                           | Provided through digital signatures                                                                              | PGP explicitly supports non-repudiation through digital signatures, whereas SSH focuses more on securing the communication channel. |
| **Usage Scenarios**         | Remote server access, secure file transfer (SCP, SFTP)                                                            | Email encryption, file encryption                                                                                | Both can be used to secure file transfers, although their primary use cases differ.                                                 |
| **Session Management**      | Establishes a secure session for continuous communication                                                         | Encrypts individual messages or files                                                                            | SSH provides an ongoing secure session, whereas PGP is generally used for encrypting individual pieces of data.                     |
| **Key Exchange**            | Diffie-Hellman key exchange algorithm                                                                             | Direct exchange or via key servers                                                                               | Both can use a form of key exchange, although the methods and contexts differ.                                                      |
| **Software Implementation** | OpenSSH, PuTTY                                                                                                    | GnuPG, PGP Desktop                                                                                               | Both have multiple software implementations available.                                                                              |
| **Cryptographic Protocol**  | Uses the SSH protocol                                                                                             | Uses the OpenPGP protocol                                                                                        | Both rely on well-defined cryptographic protocols for secure communication.                                                         |
| **User Experience**         | Requires setup of SSH keys on both client and server                                                              | Requires sharing and verifying public keys                                                                       | Both require some form of user interaction to share and verify keys, though the process and tools used can be different.            |
| **Data Transmission**       | Encrypts data during transmission                                                                                 | Encrypts data for storage and transmission                                                                       | Both encrypt data to ensure privacy and security, though the specific contexts (real-time vs stored data) can differ.               |
| **Key Pair Requirement**    | Requires a private and public key pair                                                                            | Requires a private and public key pair                                                                           | Both use asymmetric cryptography which involves generating a pair of keys: one private and one public.                              |
| **Encryption Method**       | Uses the receiver's public key to establish a session key                                                         | Uses the receiver's public key to encrypt the outgoing message                                                   | Both encrypt data with the recipient's public key, ensuring that only the corresponding private key can decrypt the data.           |
| **Data Confidentiality**    | Not readable by anyone else unless they have the private key corresponding to the public key used in the exchange | Not readable by anyone else unless they have the private key corresponding to the public key used for encryption | Both ensure that encrypted data can only be decrypted and read by someone who possesses the corresponding private key.              |

This extended table includes key principles that underline the functioning of SSH and PGP encryption, emphasizing their common reliance on asymmetric cryptography for secure communication.
