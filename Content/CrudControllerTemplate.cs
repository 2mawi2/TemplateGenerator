using Common.Controllers;
using Common.Model.<#package#>;
using Persistence<#package#>.Repositories;

namespace <#package#>.Controllers
{
    public class <#name#>Controller : CrudController<#name#>, I<#name#>Controller
    {
        public <#name#>Controller(<#name#>Repository repository) : base(repository)
        {
        }
    }
}