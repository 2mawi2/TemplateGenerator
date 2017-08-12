using Backend.Controllers;
using Common.Model.<#package#>;
using <#package#>;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Security;

namespace AdminApi.Controllers.<#package#>
{
    /// <summary>
    /// <#name#> related methods.
    /// </summary>
    [Authorize(Policy = Permissions.Erp<#name#>View)]
    [Route("api/v1/<#packageLC#>/contents")]
    public class <#name#>ApiController : CrudApiController<<#name#>>
    {
        private I<#name#>Controller _contentController;

        public <#name#>ApiController(IErp <#packageLC#>) : base(<#packageLC#>.Get<#name#>s(), Permissions.Erp<#name#>Edit)
        {
            _contentController = <#packageLC#>.Get<#name#>s();
        }
    }
}