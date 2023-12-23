

/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: get_organization
// ====================================================

export interface get_organization_organization_current_user {
  email: string;
  full_name: string | null;
  is_admin: boolean;
  is_owner: boolean | null;
  last_login: any | null;
}

export interface get_organization_organization_members_invitation {
  id: string;
  guid: string;
  invitee_identifier: string;
  created: any;
  modified: any;
}

export interface get_organization_organization_members {
  email: string;
  full_name: string | null;
  is_admin: boolean;
  is_owner: boolean | null;
  invitation: get_organization_organization_members_invitation | null;
  last_login: any | null;
}

export interface get_organization_organization_usage_api_requests {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organization_organization_usage_order_volumes {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organization_organization_usage_shipment_count {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organization_organization_usage_shipment_spend {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organization_organization_usage {
  members: number | null;
  order_volume: number | null;
  total_requests: number | null;
  total_shipments: number | null;
  unfulfilled_orders: number | null;
  api_requests: get_organization_organization_usage_api_requests[] | null;
  order_volumes: get_organization_organization_usage_order_volumes[] | null;
  shipment_count: get_organization_organization_usage_shipment_count[] | null;
  shipment_spend: get_organization_organization_usage_shipment_spend[] | null;
}

export interface get_organization_organization {
  id: string;
  name: string;
  slug: string;
  token: string;
  current_user: get_organization_organization_current_user;
  members: get_organization_organization_members[];
  usage: get_organization_organization_usage;
}

export interface get_organization {
  organization: get_organization_organization | null;
}

export interface get_organizationVariables {
  id: string;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: get_organizations
// ====================================================

export interface get_organizations_organizations_current_user {
  email: string;
  full_name: string | null;
  is_admin: boolean;
  is_owner: boolean | null;
  last_login: any | null;
}

export interface get_organizations_organizations_members_invitation {
  id: string;
  guid: string;
  invitee_identifier: string;
  created: any;
  modified: any;
}

export interface get_organizations_organizations_members {
  email: string;
  full_name: string | null;
  is_admin: boolean;
  is_owner: boolean | null;
  invitation: get_organizations_organizations_members_invitation | null;
  last_login: any | null;
}

export interface get_organizations_organizations_usage_api_requests {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organizations_organizations_usage_order_volumes {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organizations_organizations_usage_shipment_count {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organizations_organizations_usage_shipment_spend {
  date: string | null;
  label: string | null;
  count: number | null;
}

export interface get_organizations_organizations_usage {
  members: number | null;
  order_volume: number | null;
  total_requests: number | null;
  total_shipments: number | null;
  unfulfilled_orders: number | null;
  api_requests: get_organizations_organizations_usage_api_requests[] | null;
  order_volumes: get_organizations_organizations_usage_order_volumes[] | null;
  shipment_count: get_organizations_organizations_usage_shipment_count[] | null;
  shipment_spend: get_organizations_organizations_usage_shipment_spend[] | null;
}

export interface get_organizations_organizations {
  id: string;
  name: string;
  slug: string;
  token: string;
  current_user: get_organizations_organizations_current_user;
  members: get_organizations_organizations_members[];
  usage: get_organizations_organizations_usage;
}

export interface get_organizations {
  organizations: get_organizations_organizations[];
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflow
// ====================================================

export interface GetWorkflow_workflow {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  actions: any | null;
  metadata: any | null;
}

export interface GetWorkflow {
  workflow: GetWorkflow_workflow | null;
}

export interface GetWorkflowVariables {
  id: string;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflows
// ====================================================

export interface GetWorkflows_workflows_page_info {
  has_next_page: boolean;
  has_previous_page: boolean;
  start_cursor: string | null;
  end_cursor: string | null;
}

export interface GetWorkflows_workflows_edges_node {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  actions: any | null;
  metadata: any | null;
}

export interface GetWorkflows_workflows_edges {
  node: GetWorkflows_workflows_edges_node;
}

export interface GetWorkflows_workflows {
  page_info: GetWorkflows_workflows_page_info;
  edges: GetWorkflows_workflows_edges[];
}

export interface GetWorkflows {
  workflows: GetWorkflows_workflows;
}

export interface GetWorkflowsVariables {
  filter?: WorkflowFilter | null;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflowConnection
// ====================================================

export interface GetWorkflowConnection_workflow_connection {
  id: string;
  name: string;
  slug: string;
  auth_type: AuthType;
  description: string | null;
  auth_host: string | null;
  auth_endpoint: string | null;
  parameters_template: string | null;
  auth_template: string | null;
  credentials: any | null;
  metadata: any | null;
}

export interface GetWorkflowConnection {
  workflow_connection: GetWorkflowConnection_workflow_connection | null;
}

export interface GetWorkflowConnectionVariables {
  id: string;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflowConnections
// ====================================================

export interface GetWorkflowConnections_workflow_connections_page_info {
  has_next_page: boolean;
  has_previous_page: boolean;
  start_cursor: string | null;
  end_cursor: string | null;
}

export interface GetWorkflowConnections_workflow_connections_edges_node {
  id: string;
  name: string;
  slug: string;
  auth_type: AuthType;
  description: string | null;
  auth_host: string | null;
  auth_endpoint: string | null;
  parameters_template: string | null;
  auth_template: string | null;
  credentials: any | null;
  metadata: any | null;
}

export interface GetWorkflowConnections_workflow_connections_edges {
  node: GetWorkflowConnections_workflow_connections_edges_node;
}

export interface GetWorkflowConnections_workflow_connections {
  page_info: GetWorkflowConnections_workflow_connections_page_info;
  edges: GetWorkflowConnections_workflow_connections_edges[];
}

export interface GetWorkflowConnections {
  workflow_connections: GetWorkflowConnections_workflow_connections;
}

export interface GetWorkflowConnectionsVariables {
  filter?: WorkflowConnectionFilter | null;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflowAction
// ====================================================

export interface GetWorkflowAction_workflow_action_connection {
  id: string;
  name: string;
  slug: string;
}

export interface GetWorkflowAction_workflow_action {
  id: string;
  name: string;
  slug: string;
  action_type: ActionType;
  description: string | null;
  api_host: string | null;
  api_endpoint: string | null;
  method: HTTPMethod | null;
  parameters_type: ParametersType | null;
  parameters_template: string | null;
  header_template: string | null;
  content_type: HTTPContentType | null;
  connection: GetWorkflowAction_workflow_action_connection | null;
  metadata: any | null;
}

export interface GetWorkflowAction {
  workflow_action: GetWorkflowAction_workflow_action | null;
}

export interface GetWorkflowActionVariables {
  id: string;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflowActions
// ====================================================

export interface GetWorkflowActions_workflow_actions_page_info {
  has_next_page: boolean;
  has_previous_page: boolean;
  start_cursor: string | null;
  end_cursor: string | null;
}

export interface GetWorkflowActions_workflow_actions_edges_node_connection {
  id: string;
  name: string;
  slug: string;
}

export interface GetWorkflowActions_workflow_actions_edges_node {
  id: string;
  name: string;
  slug: string;
  action_type: ActionType;
  description: string | null;
  api_host: string | null;
  api_endpoint: string | null;
  method: HTTPMethod | null;
  parameters_type: ParametersType | null;
  parameters_template: string | null;
  header_template: string | null;
  content_type: HTTPContentType | null;
  connection: GetWorkflowActions_workflow_actions_edges_node_connection | null;
  metadata: any | null;
}

export interface GetWorkflowActions_workflow_actions_edges {
  node: GetWorkflowActions_workflow_actions_edges_node;
}

export interface GetWorkflowActions_workflow_actions {
  page_info: GetWorkflowActions_workflow_actions_page_info;
  edges: GetWorkflowActions_workflow_actions_edges[];
}

export interface GetWorkflowActions {
  workflow_actions: GetWorkflowActions_workflow_actions;
}

export interface GetWorkflowActionsVariables {
  filter?: WorkflowActionFilter | null;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflowEvent
// ====================================================

export interface GetWorkflowEvent_workflow_event {
  id: string;
  status: WorkflowEventStatus;
  event_type: WorflowEventType;
  parameters: any | null;
}

export interface GetWorkflowEvent {
  workflow_event: GetWorkflowEvent_workflow_event | null;
}

export interface GetWorkflowEventVariables {
  id: string;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetWorkflowEvents
// ====================================================

export interface GetWorkflowEvents_workflow_events_page_info {
  has_next_page: boolean;
  has_previous_page: boolean;
  start_cursor: string | null;
  end_cursor: string | null;
}

export interface GetWorkflowEvents_workflow_events_edges_node {
  id: string;
  status: WorkflowEventStatus;
  event_type: WorflowEventType;
  parameters: any | null;
}

export interface GetWorkflowEvents_workflow_events_edges {
  node: GetWorkflowEvents_workflow_events_edges_node;
}

export interface GetWorkflowEvents_workflow_events {
  page_info: GetWorkflowEvents_workflow_events_page_info;
  edges: GetWorkflowEvents_workflow_events_edges[];
}

export interface GetWorkflowEvents {
  workflow_events: GetWorkflowEvents_workflow_events;
}

export interface GetWorkflowEventsVariables {
  filter?: WorkflowEventFilter | null;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: delete_organization
// ====================================================

export interface delete_organization_delete_organization_organization {
  id: string;
}

export interface delete_organization_delete_organization_errors {
  field: string;
  messages: string[];
}

export interface delete_organization_delete_organization {
  organization: delete_organization_delete_organization_organization | null;
  errors: delete_organization_delete_organization_errors[] | null;
}

export interface delete_organization {
  delete_organization: delete_organization_delete_organization;
}

export interface delete_organizationVariables {
  data: DeleteOrganizationMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: create_organization
// ====================================================

export interface create_organization_create_organization_organization {
  id: string;
}

export interface create_organization_create_organization_errors {
  field: string;
  messages: string[];
}

export interface create_organization_create_organization {
  organization: create_organization_create_organization_organization | null;
  errors: create_organization_create_organization_errors[] | null;
}

export interface create_organization {
  create_organization: create_organization_create_organization;
}

export interface create_organizationVariables {
  data: CreateOrganizationMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: update_organization
// ====================================================

export interface update_organization_update_organization_organization {
  id: string;
}

export interface update_organization_update_organization_errors {
  field: string;
  messages: string[];
}

export interface update_organization_update_organization {
  organization: update_organization_update_organization_organization | null;
  errors: update_organization_update_organization_errors[] | null;
}

export interface update_organization {
  update_organization: update_organization_update_organization;
}

export interface update_organizationVariables {
  data: UpdateOrganizationMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: change_organization_owner
// ====================================================

export interface change_organization_owner_change_organization_owner_organization {
  id: string;
}

export interface change_organization_owner_change_organization_owner_errors {
  field: string;
  messages: string[];
}

export interface change_organization_owner_change_organization_owner {
  organization: change_organization_owner_change_organization_owner_organization | null;
  errors: change_organization_owner_change_organization_owner_errors[] | null;
}

export interface change_organization_owner {
  change_organization_owner: change_organization_owner_change_organization_owner;
}

export interface change_organization_ownerVariables {
  data: ChangeOrganizationOwnerMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: set_organization_user_roles
// ====================================================

export interface set_organization_user_roles_set_organization_user_roles_organization {
  id: string;
}

export interface set_organization_user_roles_set_organization_user_roles_errors {
  field: string;
  messages: string[];
}

export interface set_organization_user_roles_set_organization_user_roles {
  organization: set_organization_user_roles_set_organization_user_roles_organization | null;
  errors: set_organization_user_roles_set_organization_user_roles_errors[] | null;
}

export interface set_organization_user_roles {
  set_organization_user_roles: set_organization_user_roles_set_organization_user_roles;
}

export interface set_organization_user_rolesVariables {
  data: SetOrganizationUserRolesMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: send_organization_invites
// ====================================================

export interface send_organization_invites_send_organization_invites_errors {
  field: string;
  messages: string[];
}

export interface send_organization_invites_send_organization_invites {
  errors: send_organization_invites_send_organization_invites_errors[] | null;
}

export interface send_organization_invites {
  send_organization_invites: send_organization_invites_send_organization_invites;
}

export interface send_organization_invitesVariables {
  data: SendOrganizationInvitesMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: get_organization_invitation
// ====================================================

export interface get_organization_invitation_organization_invitation_invitee {
  email: string;
}

export interface get_organization_invitation_organization_invitation {
  invitee_identifier: string;
  organization_name: string;
  invitee: get_organization_invitation_organization_invitation_invitee | null;
}

export interface get_organization_invitation {
  organization_invitation: get_organization_invitation_organization_invitation | null;
}

export interface get_organization_invitationVariables {
  guid: string;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: accept_organization_invitation
// ====================================================

export interface accept_organization_invitation_accept_organization_invitation_organization {
  id: string;
}

export interface accept_organization_invitation_accept_organization_invitation_errors {
  field: string;
  messages: string[];
}

export interface accept_organization_invitation_accept_organization_invitation {
  organization: accept_organization_invitation_accept_organization_invitation_organization | null;
  errors: accept_organization_invitation_accept_organization_invitation_errors[] | null;
}

export interface accept_organization_invitation {
  accept_organization_invitation: accept_organization_invitation_accept_organization_invitation;
}

export interface accept_organization_invitationVariables {
  data: AcceptOrganizationInvitationMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: delete_organization_invitation
// ====================================================

export interface delete_organization_invitation_delete_organization_invitation {
  id: string;
}

export interface delete_organization_invitation {
  delete_organization_invitation: delete_organization_invitation_delete_organization_invitation;
}

export interface delete_organization_invitationVariables {
  data: DeleteMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: CreateWorkflow
// ====================================================

export interface CreateWorkflow_create_workflow_errors {
  field: string;
  messages: string[];
}

export interface CreateWorkflow_create_workflow {
  errors: CreateWorkflow_create_workflow_errors[] | null;
}

export interface CreateWorkflow {
  create_workflow: CreateWorkflow_create_workflow;
}

export interface CreateWorkflowVariables {
  data: CreateWorkflowMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: UpdateWorkflow
// ====================================================

export interface UpdateWorkflow_update_workflow_errors {
  field: string;
  messages: string[];
}

export interface UpdateWorkflow_update_workflow {
  errors: UpdateWorkflow_update_workflow_errors[] | null;
}

export interface UpdateWorkflow {
  update_workflow: UpdateWorkflow_update_workflow;
}

export interface UpdateWorkflowVariables {
  data: UpdateWorkflowMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: DeleteWorkflow
// ====================================================

export interface DeleteWorkflow_delete_workflow {
  id: string;
}

export interface DeleteWorkflow {
  delete_workflow: DeleteWorkflow_delete_workflow;
}

export interface DeleteWorkflowVariables {
  data: DeleteMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: CreateWorkflowConnection
// ====================================================

export interface CreateWorkflowConnection_create_workflow_connection_errors {
  field: string;
  messages: string[];
}

export interface CreateWorkflowConnection_create_workflow_connection {
  errors: CreateWorkflowConnection_create_workflow_connection_errors[] | null;
}

export interface CreateWorkflowConnection {
  create_workflow_connection: CreateWorkflowConnection_create_workflow_connection;
}

export interface CreateWorkflowConnectionVariables {
  data: CreateWorkflowConnectionMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: UpdateWorkflowConnection
// ====================================================

export interface UpdateWorkflowConnection_update_workflow_connection_errors {
  field: string;
  messages: string[];
}

export interface UpdateWorkflowConnection_update_workflow_connection {
  errors: UpdateWorkflowConnection_update_workflow_connection_errors[] | null;
}

export interface UpdateWorkflowConnection {
  update_workflow_connection: UpdateWorkflowConnection_update_workflow_connection;
}

export interface UpdateWorkflowConnectionVariables {
  data: UpdateWorkflowConnectionMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: DeleteWorkflowConnection
// ====================================================

export interface DeleteWorkflowConnection_delete_workflow_connection {
  id: string;
}

export interface DeleteWorkflowConnection {
  delete_workflow_connection: DeleteWorkflowConnection_delete_workflow_connection;
}

export interface DeleteWorkflowConnectionVariables {
  data: DeleteMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: CreateWorkflowAction
// ====================================================

export interface CreateWorkflowAction_create_workflow_action_errors {
  field: string;
  messages: string[];
}

export interface CreateWorkflowAction_create_workflow_action {
  errors: CreateWorkflowAction_create_workflow_action_errors[] | null;
}

export interface CreateWorkflowAction {
  create_workflow_action: CreateWorkflowAction_create_workflow_action;
}

export interface CreateWorkflowActionVariables {
  data: CreateWorkflowActionMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: UpdateWorkflowAction
// ====================================================

export interface UpdateWorkflowAction_update_workflow_action_errors {
  field: string;
  messages: string[];
}

export interface UpdateWorkflowAction_update_workflow_action {
  errors: UpdateWorkflowAction_update_workflow_action_errors[] | null;
}

export interface UpdateWorkflowAction {
  update_workflow_action: UpdateWorkflowAction_update_workflow_action;
}

export interface UpdateWorkflowActionVariables {
  data: UpdateWorkflowActionMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: DeleteWorkflowAction
// ====================================================

export interface DeleteWorkflowAction_delete_workflow_action {
  id: string;
}

export interface DeleteWorkflowAction {
  delete_workflow_action: DeleteWorkflowAction_delete_workflow_action;
}

export interface DeleteWorkflowActionVariables {
  data: DeleteMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: CreateWorkflowEvent
// ====================================================

export interface CreateWorkflowEvent_create_workflow_event_errors {
  field: string;
  messages: string[];
}

export interface CreateWorkflowEvent_create_workflow_event {
  errors: CreateWorkflowEvent_create_workflow_event_errors[] | null;
}

export interface CreateWorkflowEvent {
  create_workflow_event: CreateWorkflowEvent_create_workflow_event;
}

export interface CreateWorkflowEventVariables {
  data: CreateWorkflowEventMutationInput;
}


/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: CancelWorkflowEvent
// ====================================================

export interface CancelWorkflowEvent_cancel_workflow_event_errors {
  field: string;
  messages: string[];
}

export interface CancelWorkflowEvent_cancel_workflow_event {
  errors: CancelWorkflowEvent_cancel_workflow_event_errors[] | null;
}

export interface CancelWorkflowEvent {
  cancel_workflow_event: CancelWorkflowEvent_cancel_workflow_event;
}

export interface CancelWorkflowEventVariables {
  data: CancelWorkflowEventMutationInput;
}

/* tslint:disable */
// This file was automatically generated and should not be edited.

//==============================================================
// START Enums and Input Objects
//==============================================================

export enum AuthType {
  api_key = "api_key",
  basic = "basic",
  jwt = "jwt",
  oauth2 = "oauth2",
}

export enum ActionType {
  data_mapping = "data_mapping",
  function_call = "function_call",
  http_request = "http_request",
}

export enum HTTPMethod {
  delete = "delete",
  get = "get",
  patch = "patch",
  post = "post",
  put = "put",
}

export enum ParametersType {
  data = "data",
  queystring = "queystring",
}

export enum HTTPContentType {
  form = "form",
  json = "json",
  text = "text",
  xml = "xml",
}

export enum WorkflowEventStatus {
  cancelled = "cancelled",
  failed = "failed",
  pending = "pending",
  running = "running",
  success = "success",
}

export enum WorflowEventType {
  auto = "auto",
  manual = "manual",
  scheduled = "scheduled",
  webhook = "webhook",
}

export enum UserRole {
  admin = "admin",
  developer = "developer",
  member = "member",
}

// null
export interface WorkflowFilter {
  date_after?: any | null;
  date_before?: any | null;
  omit?: string[] | null;
  keyword?: string | null;
}

// null
export interface WorkflowConnectionFilter {
  date_after?: any | null;
  date_before?: any | null;
  omit?: string[] | null;
  keyword?: string | null;
  auth_type?: AuthType | null;
}

// null
export interface WorkflowActionFilter {
  date_after?: any | null;
  date_before?: any | null;
  omit?: string[] | null;
  keyword?: string | null;
  action_type?: ActionType | null;
}

// null
export interface WorkflowEventFilter {
  date_after?: any | null;
  date_before?: any | null;
  omit?: string[] | null;
  keyword?: string | null;
  status?: WorkflowEventStatus | null;
  event_type?: WorflowEventType | null;
}

// null
export interface DeleteOrganizationMutationInput {
  id: string;
  password: string;
}

// null
export interface CreateOrganizationMutationInput {
  name: string;
}

// null
export interface UpdateOrganizationMutationInput {
  id: string;
  name?: string | null;
}

// null
export interface ChangeOrganizationOwnerMutationInput {
  org_id: string;
  email: string;
  password: string;
}

// null
export interface SetOrganizationUserRolesMutationInput {
  org_id: string;
  user_id: string;
  roles: UserRole[];
}

// null
export interface SendOrganizationInvitesMutationInput {
  org_id: string;
  emails: string[];
  redirect_url: string;
}

// null
export interface AcceptOrganizationInvitationMutationInput {
  guid: string;
}

// null
export interface DeleteMutationInput {
  id: string;
}

// null
export interface CreateWorkflowMutationInput {
  name: string;
  actions: any;
  description?: string | null;
  metadata?: any | null;
}

// null
export interface UpdateWorkflowMutationInput {
  id: string;
  name?: string | null;
  actions?: any | null;
  description?: string | null;
  metadata?: any | null;
}

// null
export interface CreateWorkflowConnectionMutationInput {
  name: string;
  description?: string | null;
  api_host?: string | null;
  api_endpoint?: string | null;
  auth_type?: AuthType | null;
  parameters_template?: string | null;
  auth_template?: string | null;
  metadata?: any | null;
}

// null
export interface UpdateWorkflowConnectionMutationInput {
  name?: string | null;
  description?: string | null;
  api_host?: string | null;
  api_endpoint?: string | null;
  auth_type?: AuthType | null;
  parameters_template?: string | null;
  auth_template?: string | null;
  metadata?: any | null;
  id: string;
}

// null
export interface CreateWorkflowActionMutationInput {
  name: string;
  api_host?: string | null;
  description?: string | null;
  api_endpoint?: string | null;
  action_type?: ActionType | null;
  method?: HTTPMethod | null;
  parameters_type?: ParametersType | null;
  parameters_template?: string | null;
  header_template?: string | null;
  content_type?: HTTPContentType | null;
  metadata?: any | null;
  connection_id?: string | null;
}

// null
export interface UpdateWorkflowActionMutationInput {
  name?: string | null;
  api_host?: string | null;
  description?: string | null;
  api_endpoint?: string | null;
  action_type?: ActionType | null;
  method?: HTTPMethod | null;
  parameters_type?: ParametersType | null;
  parameters_template?: string | null;
  header_template?: string | null;
  content_type?: HTTPContentType | null;
  metadata?: any | null;
  connection_id?: string | null;
  id: string;
}

// null
export interface CreateWorkflowEventMutationInput {
  name: string;
  parameters?: any | null;
  event_type?: WorflowEventType | null;
}

// null
export interface CancelWorkflowEventMutationInput {
  id: string;
}

//==============================================================
// END Enums and Input Objects
//==============================================================