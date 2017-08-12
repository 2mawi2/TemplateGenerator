using Backend.Controllers;
using Common.Model.ERP;
using ERP;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Security;

namespace AdminApi.Controllers.ERP
{
    /// <summary>
    /// <#name#> related methods.
    /// </summary>
    [Authorize(Policy = Permissions.ErpContentView)]
    [Route("api/v1/erp/contents")]
    public class ContentApiController : CrudApiController<Content>
    {
        private IContentController _contentController;

        public ContentApiController(IErp erp) : base(erp.GetContents(), Permissions.ErpContentEdit)
        {
            _contentController = erp.GetContents();
        }
    }
}