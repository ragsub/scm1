import threading
from contextlib import contextmanager
from SCM.Tenant.exceptions import TenantNotFoundError

state_local = threading.local()

def create_user_session(request, tenant):
    request.session['current_tenant'] = tenant

def get_tenant_from_session(request):
    tenant = request.session.get('current_tenant')
    return tenant

def get_state():
    default_state = {
        'enabled':True,
        'tenant':None
    }
    state = getattr(state_local, 'state', default_state)
    return state

def remove_state():
    delattr(state_local,'state')

def get_current_tenant():
    state = get_state()

    if state["enabled"] and state["tenant"] is None:
        raise TenantNotFoundError("Tenant is enabled and empty")

    return state["tenant"]

@contextmanager
def tenant_context(tenant=None, enabled=True):
    previous_state = get_state()
    new_state = previous_state.copy()
    new_state["enabled"] = enabled
    new_state["tenant"] = tenant
    state_local.state = new_state

    try:
        yield
    finally:
        if previous_state:
            state_local.state = previous_state
        else:
            delattr(state_local, "state")

@contextmanager
def no_tenant_context():
    with tenant_context(enabled=False):
        yield