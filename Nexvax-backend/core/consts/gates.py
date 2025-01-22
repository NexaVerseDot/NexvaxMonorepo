from typing import Dict, Type
from core.lib.inouts import BasePayGate, StripeGate

# Payment Gate Registry
GATES: Dict[int, Type[BasePayGate]] = {}

# Register payment gates
GATES[StripeGate.ID] = StripeGate

# Gate name to ID mapping for reverse lookup
GATE_IDS = {
    gate_cls.NAME: gate_id
    for gate_id, gate_cls in GATES.items()
}
