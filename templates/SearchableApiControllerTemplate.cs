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
    [Authorize(Policy = Permissions.<#packageFLUC#><#name#>View)]
    [Route("api/v1/<#packageLC#>/<#nameLC#>")]
    public class <#name#>ApiController : SearchableApiController<<#name#>, <#name#>.SortBy, <#name#>.FilterAttribute>
    {
        public <#name#>ApiController(I<#packageFLUC#> <#packageLC#>) : base(<#packageLC#>.Get<#name#>s(), Permissions.<#packageFLUC#><#name#>Edit)
        {
        }
    }
}