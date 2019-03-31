import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ClockCycles, Event, ReadOnly
from cocotb.clock import Clock
from cocotb.result import TestError, TestFailure, TestSuccess
from random import randint

@cocotb.test()
def test(dut):
    yield Timer(1, units='ns')

