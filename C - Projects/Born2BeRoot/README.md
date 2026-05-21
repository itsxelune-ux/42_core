*This project has been created as part of the 42 curriculum by omitrovs.*

# Born2beRoot

## Description

Born2beRoot is a system administration project. The goal of this project is to introduce students to virtualization, Linux server installation, and essential system security.  
Through this project, students learn how a Linux system works, how to configure it properly, and how to apply rules that help keep the system secure and stable.

---

## Operating System Choice

For this project, I chose **Debian**. Debian was recommended from authors of this project for its beginner friendliness.

Debian is a Linux distribution, an operating system built on the Linux kernel. Known for its stability and reliability, it is a strong choice for server environments. Its large community and extensive documentation make it easier to understand system behavior and troubleshoot issues.

One downside of Debian is that it favors stability over the latest software versions, but specifically for this project, the tradeoff is acceptable.

---

## Main Design Choices

### Partitioning

I used Logical Volume Manager (LVM) to manage disk partitions. Separate partitions were created for directories such as `/`, `/home`, `/var`, and `/tmp`, along with a swap partition. This setup helps keep the system organized, improves security, and makes it easier to manage disk space if changes are needed later.

### User Management

Instead of working directly as root, I created a regular user account and added it to the required groups, including `sudo`. This allows administrative tasks to be performed safely while reducing the risks associated with using the root account. Password expiration and complexity rules apply to all users.

### Security Configuration

**AppArmor** acts like a security profile that defines exactly what a program is allowed to acces and blocks everything else.
I enabled AppArmor to restrict what applications can access on the system. I also configured a strong password policy that enforces complex passwords and regular changes.  
For SSH access, I changed the default port and disabled direct root login to reduce the risk of unauthorized access.

### Services

A service is a background process that provides a specific functionality, such as remote acces, firewall management etc.
Only essential services were kept on the system. SSH allows remote access, UFW manages firewall rules, and cron handles scheduled tasks.

---

## Debian vs Rocky Linux

- Debian is a community-driven Linux distribution that focuses on stability and simplicity. It is widely used for servers and works well for learning system administration fundamentals.

- Rocky Linux is designed as a free, open-source alternative to Red Hat Enterprise Linux. It targets enterprise environments and uses SELinux by default, offering very strong security features. However, it requires more experience to configure correctly.

---

### Mandatory Access Control (MAC)

Mandatory Access Control is a security model based on predefined rules. These rules define how users and processes can access files, directories, ports, and other system resources. The system administrator defines these rules, and applications must follow them strictly.

### AppArmor vs SELinux

Securing a Linux environment requires more than standard user permissions. This is where Linux Security Modules (LSMs) such as AppArmor and SELinux come in. They act like gatekeepers by controlling what applications are allowed to do.

- **AppArmor** enforces Mandatory Access Control using a profile based approach. Each application has a profile that specifies exactly which files and system resources it can access. AppArmor mainly focuses on file access and system calls. 

- **SELinux** (Security-Enhanced Linux) also enforces Mandatory Access Control, but it uses a label-based approach. Every file, process, and resource receives a security context. It offers very fine-grained control over system behavior, including file access, network connections, and allowed system calls. While this makes it extremely powerful, it also makes it more complex to configure and maintain.

---

## UFW vs firewalld

- **Firewall** is like a gatekeeper for the system, controlling which network connections are allowed and which are blocked. 

- **UFW** is a tool on Debian that makes it easy to set up and manage these rules.

---

## VirtualBox vs UTM

- **VirtualBox** is a virtualization tool that works on Windows, macOS, and Linux. It is feature-rich, lets you run multiple virtual machines, and is great for testing or learning different operating systems.

- **UTM** is also a virtualization tool, but it’s designed mainly for macOS and iOS. It’s simpler to use, optimized for Apple devices, and good for running virtual machines easily on Mac, though it has fewer advanced features than VirtualBox.

---

## Instructions

0. Before starting, it is a must to compare the signatures of .vdi file and uploaded signature
into git. To do this, use this commands:
```bash
cd ~/sgoinfre/b2broot
sha1sum b2broot.vdi
```
1. Open VirtualBox and clone my machine
2. Start the machine
3. SSH: from the physical machine, open terminal and connect via SSH using the mandatory
port:
```bash
ssh <your_login>@localhost -p 4242
```

### Resources

https://www.debian.org/doc/
https://betterstack.com/community/guides/linux/ufw-vs-firewalld/
https://tuxcare.com/blog/selinux-vs-apparmor/
https://www.geeksforgeeks.org/linux-unix/crontab-in-linux-with-examples/
https://manpages.debian.org/testing/libpam-pwquality/pam_pwquality.8.en.html


### AI usage 

This project was primarily completed manually. I used AI only in a limited way to:
- Rephrase explanations for clarity
- Summarize concepts for documentation

All tehnical work, system setup and testing are done without using AI.